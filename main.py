import pandas as pd

# Load data
df = pd.read_csv('../data/car_data.csv')

# Sanity check first
print(df.shape)
print(df.info())
df.head()
