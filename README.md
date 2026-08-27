# Car Dekho Market Trends Analysis

Data analysis case study on a used-vehicle listings dataset (Car Dekho), 
answering 25 business questions covering data quality, pricing, 
depreciation trends, and vehicle-type-specific insights (bikes vs cars).

## Structure
- `data/car_data.csv` — raw dataset (301 records)
- `main.py` — full analysis script, organized by checkpoint
- `outputs/` — charts/exports (if any)

## Key Findings
- 301 listings, 98 unique models, years 2003–2018, no missing data
- 101 two-wheelers, 200 cars (split by model naming convention)
- Depreciation driven mainly by vehicle age and kms driven
- Selling price weakly tied to age, barely tied to kms driven
- Best resale-value retention: single-owner, low-mileage, recent-model vehicles
