# Hotel Source-of-Truth Matrix

| Operating fact | Preferred source of truth | AI rule |
|---|---|---|
| Reservation status | PMS / CRS | Never infer from messages alone |
| Room / apartment status | PMS + housekeeping confirmation | Treat conflicts as exceptions |
| Rate and restriction | RMS / approved rate source | Label date/time of rate evidence |
| Work order | CMMS | Do not mark closed without system evidence |
| Preventive maintenance | CMMS / engineering plan | Verify asset and schedule |
| Guest complaint | CRM / approved complaint log | Minimize personal data |
| Compensation authority | Approved policy / delegation matrix | AI never grants authority |
| Utility consumption | Meter / utility invoice / BMS export | Normalize against occupancy before conclusions |
| Inventory | Inventory system / controlled count | Show count date |
| Financial actuals | Finance ledger / approved report | Do not invent missing periods |
| Employee roster | Approved workforce system | Protect employee data |
| SOP requirement | Controlled document repository | Use current approved revision only |
