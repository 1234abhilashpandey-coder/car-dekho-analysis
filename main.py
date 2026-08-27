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
