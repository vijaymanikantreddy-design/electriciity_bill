# Electricity Bill Calculator

This is a Python project to calculate electricity bills based on tiered pricing with a fixed charge.

## Features
- Tiered pricing:
  - 0-100 units: $1.50/unit
  - 101-200 units: $2.50/unit
  - 201-300 units: $4.00/unit
  - 301+ units: $6.00/unit
- Fixed charge: $50
- Unit tests included with `pytest`
- Ready for Docker and Jenkins automation

## Usage

### Run Locally
```bash
python electricity_bill.py 250
