#!/usr/bin/env python3
"""Validate hotel prompt registry paths, titles, numbering and JSON/CSV agreement."""
import csv
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []

try:
    records = json.loads((ROOT / 'data/prompts.json').read_text(encoding='utf-8'))
    with (ROOT / 'data/prompts.csv').open(encoding='utf-8', newline='') as stream:
        reader = csv.DictReader(stream)
        fields = reader.fieldnames
        csv_records = list(reader)
    if len(records) != 260 or len({p['id'] for p in records}) != 260:
        errors.append('Expected 260 records with unique IDs')
    if sorted(p['global_number'] for p in records) != list(range(1, 261)):
        errors.append('Prompt numbers must cover 001–260 exactly once')
    if len(csv_records) != len(records):
        errors.append('JSON and CSV record counts differ')
    for index, p in enumerate(records):
        expected_chapters = list((ROOT / 'playbook').glob(f"{p['article_number']:02d}-*.md"))
        if len(expected_chapters) != 1 or p['source_article'] != expected_chapters[0].relative_to(ROOT).as_posix():
            errors.append(f"Prompt {p['global_number']}: invalid source_article")
        path = ROOT / p['prompt_file']
        if not path.is_file():
            errors.append(f"Missing prompt file: {p['prompt_file']}")
            continue
        if not path.name.startswith(f"{p['global_number']:03d}-"):
            errors.append(f"Prompt {p['global_number']}: filename number differs")
        text = path.read_text(encoding='utf-8')
        title = re.sub(r'^#+ (?:Prompt \d+ [—–-] )?', '', text.splitlines()[0])
        if title != p['title']:
            errors.append(f"Prompt {p['global_number']}: title differs from canonical file")
        risk = re.search(r'\*\*Risk level:\*\*\s*([^\n]+)', text)
        if risk and risk[1].strip().casefold() != p['risk_level'].casefold():
            errors.append(f"Prompt {p['global_number']}: risk level differs from canonical file")
        # ESG metadata was revised with Article 14 and must match the new files.
        if 131 <= p['global_number'] <= 140:
            for key, label in [('id', 'Prompt ID'), ('department', 'Department'), ('risk_level', 'Risk level'), ('status', 'Status')]:
                match = re.search(rf'\*\*{label}:\*\*\s*([^\n]+)', text)
                if not match or match[1].strip().strip('`') != p[key]:
                    errors.append(f"Prompt {p['global_number']}: {key} differs from canonical file")
        if index < len(csv_records) and any(csv_records[index][key] != str(p[key]) for key in fields):
            errors.append(f"Prompt {p['global_number']}: JSON and CSV differ")
    files = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'prompt-library').glob('*.md')}
    if files != {p['prompt_file'] for p in records}:
        errors.append('Registry does not cover the complete individual prompt library')
except Exception as exc:
    errors.append(f'Invalid registry: {exc}')

if errors:
    raise SystemExit('\n'.join(errors))
print('Registry validation passed: 26 chapters, 260 unique prompts, all file paths and titles, ESG metadata, JSON/CSV agreement.')
