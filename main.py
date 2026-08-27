import pandas as pd

# Load data
df = pd.read_csv('data/car_data.csv')

# --- Sanity check ---
print("Shape:", df.shape)
print(df.info())
print(df.head())
print("\n" + "="*50 + "\n")

# Q1. Manufacturing year range
print("Q1. Earliest year:", df['Year'].min())
print("Q1. Latest year:", df['Year'].max())

# Q2. Lowest selling price
print("\nQ2. Lowest selling price:", df['Selling_Price'].min())

# Q3. Highest selling price
print("Q3. Highest selling price:", df['Selling_Price'].max())

# Q4. Number of records
print("\nQ4. Total records:", len(df))

# Q5. Missing values check
print("\nQ5. Missing values per column:")
print(df.isnull().sum())
print("Q5. Total missing values:", df.isnull().sum().sum())

# Q6. Number of unique vehicles
print("\nQ6. Unique vehicles:", df['Car_Name'].nunique())

# Q7. Most sold vehicle
print("\nQ7. Top 10 most listed vehicles:")
print(df['Car_Name'].value_counts().head(10))
print("Q7. Most listed vehicle:", df['Car_Name'].value_counts().idxmax())

# Q8. CNG vehicles
print("\nQ8. Fuel types present:", df['Fuel_Type'].unique())
cng_count = (df['Fuel_Type'] == 'CNG').sum()
print("Q8. CNG vehicles:", cng_count)

# Q9. Vehicles sold by individuals directly
print("\nQ9. Seller types present:", df['Seller_Type'].unique())
individual_count = (df['Seller_Type'] == 'Individual').sum()
print("Q9. Individual sellers:", individual_count)

# Q10. Automatic transmission vehicles
print("\nQ10. Transmission types present:", df['Transmission'].unique())
auto_count = (df['Transmission'] == 'Automatic').sum()
print("Q10. Automatic transmission vehicles:", auto_count)

# Q11. Single-owner vehicles
print("\nQ11. Owner values present:", df['Owner'].unique())
print("Q11. Owner value distribution:")
print(df['Owner'].value_counts())
single_owner_count = (df['Owner'] == 0).sum()
print("Q11. Single-owner vehicles:", single_owner_count)

# Create depreciation columns
df['Depreciation'] = df['Present_Price'] - df['Selling_Price']
df['Depreciation_Pct'] = (df['Depreciation'] / df['Present_Price']) * 100

# Q12. Most and least cost depreciated vehicle
print("\nQ12. Most depreciated vehicle (absolute):")
print(df.loc[df['Depreciation'].idxmax(), ['Car_Name','Year','Present_Price','Selling_Price','Depreciation']])

print("\nQ12. Least depreciated vehicle (absolute):")
print(df.loc[df['Depreciation'].idxmin(), ['Car_Name','Year','Present_Price','Selling_Price','Depreciation']])

# Q13. Brands less affected by depreciation
# Extract brand as first word of Car_Name (works reasonably for this dataset)
df['Brand'] = df['Car_Name'].apply(lambda x: x.split()[0])
brand_depreciation = df.groupby('Brand')['Depreciation_Pct'].mean().sort_values()
print("\nQ13. Average % depreciation by brand (lowest = least affected):")
print(brand_depreciation)

# Q14. Correlation to explore factors affecting depreciation
print("\nQ14. Correlation of numeric features with Depreciation_Pct:")
numeric_cols = ['Year','Kms_Driven','Owner','Present_Price','Depreciation_Pct']
print(df[numeric_cols].corr()['Depreciation_Pct'].sort_values(ascending=False))

# Q15. Does selling price correlate with age and kms driven?
df['Age'] = 2018 - df['Year']  # dataset's latest year as reference
print("\nQ15. Correlation of Selling_Price with Age and Kms_Driven:")
print(df[['Selling_Price','Age','Kms_Driven']].corr()['Selling_Price'])

# Q16. Vehicles manufactured after 2014
newest = df[df['Year'] > 2014]
print(f"\nQ16. Vehicles manufactured after 2014: {len(newest)}")
print(newest[['Car_Name','Year','Selling_Price']].sort_values('Year'))

print("\n" + "="*50)
print("CHECKPOINT 3: Two-Wheeler Analysis")
print("="*50)

# Derive vehicle type from naming convention
df['Vehicle_Type'] = df['Car_Name'].apply(lambda x: 'Bike' if x[0].isupper() else 'Car')
print("\nVehicle type counts:")
print(df['Vehicle_Type'].value_counts())

# Q17. Data of only two-wheelers
bikes = df[df['Vehicle_Type'] == 'Bike']
print(f"\nQ17. Two-wheeler records: {len(bikes)}")
print(bikes[['Car_Name','Year','Selling_Price']].head(10))

# Q18. Oldest bike sold
oldest_bike = bikes.loc[bikes['Year'].idxmin()]
print("\nQ18. Oldest bike sold:")
print(oldest_bike[['Car_Name','Year','Selling_Price']])

# Q19. Newest bike sold
newest_bike = bikes.loc[bikes['Year'].idxmax()]
print("\nQ19. Newest bike sold:")
print(newest_bike[['Car_Name','Year','Selling_Price']])

# Q20. Most sold bike
print("\nQ20. Most listed bike model:")
print(bikes['Car_Name'].value_counts().head(5))

# Q21. Deals that exceeded general expectation (unusual selling price relative to present price)
bikes = bikes.copy()
bikes['Price_Ratio'] = bikes['Selling_Price'] / bikes['Present_Price']
print("\nQ21. Bike price ratio (Selling/Present) stats:")
print(bikes['Price_Ratio'].describe())

# Flag bikes that sold for unusually HIGH relative price (good deal for seller / high demand)
# using > mean + 1 std as a simple outlier threshold
threshold_high = bikes['Price_Ratio'].mean() + bikes['Price_Ratio'].std()
good_deals = bikes[bikes['Price_Ratio'] > threshold_high].sort_values('Price_Ratio', ascending=False)
print(f"\nQ21. Bikes selling above expectation (ratio > {threshold_high:.2f}):")
print(good_deals[['Car_Name','Year','Present_Price','Selling_Price','Price_Ratio']])
