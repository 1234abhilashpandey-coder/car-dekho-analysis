import pandas as pd

# Load data
df = pd.read_csv('../data/car_data.csv')

# Sanity check first
print(df.shape)
print(df.info())
df.head()

# Q1. Manufacturing year range
print("Earliest year:", df['Year'].min())
print("Latest year:", df['Year'].max())

# Q2. Lowest selling price
print("Lowest selling price:", df['Selling_Price'].min())

# Q3. Highest selling price
print("Highest selling price:", df['Selling_Price'].max())

# Q4. Number of records
print("Total records:", df.shape[0])

# Q5. Missing values check
print(df.isnull().sum())
print("Total missing values:", df.isnull().sum().sum())

# Q6. Number of unique vehicles
print("Unique vehicles:", df['Car_Name'].nunique())

# Q7. Most sold vehicle
print(df['Car_Name'].value_counts().head(10))
print("Most listed vehicle:", df['Car_Name'].value_counts().idxmax())

# Q8. CNG vehicles
print(df['Fuel_Type'].unique())  # check exact spelling first
cng_count = (df['Fuel_Type'] == 'CNG').sum()
print("CNG vehicles:", cng_count)

# Q9. Vehicles sold by individuals directly
print(df['Seller_Type'].unique())  # check exact spelling first
individual_count = (df['Seller_Type'] == 'Individual').sum()
print("Individual sellers:", individual_count)

# Q10. Automatic transmission vehicles
print(df['Transmission'].unique())  # check exact spelling first
auto_count = (df['Transmission'] == 'Automatic').sum()
print("Automatic transmission vehicles:", auto_count)

# Q11. Single-owner vehicles
print(df['Owner'].unique())         # see what values exist (0, 1, 3 etc.)
print(df['Owner'].value_counts())   # see distribution
single_owner_count = (df['Owner'] == 0).sum()
print("Single-owner vehicles:", single_owner_count)
