# Car Dekho Market Trends Analysis

A data analysis case study on a used-vehicle listings dataset (Car Dekho). The dataset is provided as a CSV file, and the project answers 25 business questions covering data quality, pricing, depreciation trends, and vehicle-type-specific insights (two-wheelers vs. cars).

**Author:** Abhilash Pandey

**AICTE STU ID:** STU6a2ae770771891781196656

**Repo:** https://github.com/1234abhilashpandey-coder/car-dekho-analysis

---

## Project Structure

```
car-dekho-analysis/
├── data/
│   └── car_data.csv          # Raw dataset (301 records, 9 columns)
├── main.py                   # Full analysis script, organized by checkpoint
├── outputs/                  # Charts/exports (if any)
├── Car_Dekho_Presentation.pptx
└── README.md
```

---

## Setup

This project uses **pandas** for all data loading, cleaning, and analysis. **Install it before running the script:**

```bash
pip install pandas
```

If `pip` doesn't work in your environment (some Codespaces/venvs need this instead):

```bash
python3 -m pip install pandas
```

Then run the analysis:

```bash
python main.py
```

---

## Questions Answered

**Data Understanding**

1. From which manufacturing year to which manufacturing year are vehicles present in this data?
2. What is the lowest price at which a vehicle is sold?
3. What is the highest price at which a vehicle is sold?
4. How many records are there in this data?
5. Are there any missing records in this data?
6. How many different vehicles are present in this data?
7. Which is the most sold vehicle in this data?
8. Does the database include any CNG vehicle? If yes, how many?
9. How many vehicles here are for sale from individuals directly?
10. Does this database contain automatic transmission vehicles? If yes, how many?
11. How many single-person-owned vehicles are there in this database?

**Depreciation & Pricing Patterns**

12. Which is the most and least cost-depreciated vehicle in the data?
13. Which brands of vehicles are less affected by cost depreciation?
14. Are there any factors that affect cost depreciation?
15. In general, is selling price affected by the age of the vehicle and distance driven? Is this observable from the data?
16. Can we get an idea about the newest vehicles (manufactured after 2014)?

**Two-Wheeler Analysis**

17. Can we find data of only two-wheelers from this data?
18. Which is the oldest bike sold here?
19. Which is the newest bike sold here?
20. Which is the most sold bike here?
21. Do you find any deal in two-wheelers that exceeded the general expectation? Can you find a reason for it?

**Car Analysis**

22. Can we find data of only cars from this data?
23. Which is the oldest car sold here?
24. Which is the newest car sold here?
25. Do you find any deal in cars that exceeded the general expectation? Can you find a reason for it?

---

## Key Findings

- **301 records**, **98 unique vehicle models**, manufacturing years ranging from **2003 to 2018**, with **no missing values**.
- Selling prices range from **₹0.1 lakh to ₹35.0 lakh**.
- **101 two-wheelers** and **200 cars** were present, identified using the naming convention that motorcycle brand names are capitalized (Bajaj, Hero, Honda, Royal Enfield, TVS, Yamaha, KTM, etc.) while car model names are lowercase (swift, alto 800, city, etc.).
- Only **2 CNG vehicles**, **40 automatic transmission** vehicles, and **106 individually-sold** listings.
- **290 vehicles** were single-owner (`Owner = 0`).
- Depreciation (Present Price − Selling Price) is most strongly driven by **vehicle age** (older → more depreciation) and **kilometers driven**, while it correlates only weakly with age and barely with kms driven when looking at raw selling price directly — meaning mileage alone is a weaker price predictor than commonly assumed.
- Premium/luxury vehicles (e.g., Land Cruiser, Camry) depreciate the most in percentage terms; two-wheeler brands like Vitara and UM retain value best proportionally.
- The best "value-retaining" deals — both in two-wheelers and cars — consistently share the same profile: **single owner, low mileage, and a recent model year**.
- **147 vehicles** in the dataset were manufactured after 2014.

---

## Tech Stack

- Python
- Pandas
