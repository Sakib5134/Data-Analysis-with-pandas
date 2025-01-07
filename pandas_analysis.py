# Import necessary libraries
import pandas as pd
import numpy as np

# Step 1: Create index, columns, and a 2D array
index = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()
columns = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()

# Create a 2D array with values ranging from 100 to 1
array_2d = np.arange(100, 0, -1).reshape(10, 10)

# Step 2: Create a DataFrame using the index, columns, and array
df = pd.DataFrame(data=array_2d, index=index, columns=columns)

# Display the DataFrame
print("Initial DataFrame:")
print(df)

# Step 3: Select specific columns and rows
# Grab a single column 'c10'
print("\nColumn c10:")
print(df['c10'])

# Grab multiple columns 'c4', 'c2', 'c9'
print("\nColumns c4, c2, c9:")
print(df[['c4', 'c2', 'c9']])

# Step 4: Add and delete a new column
# Add a new column 'new' as c1 * c10
df['new'] = df['c1'] * df['c10']
print("\nDataFrame after adding 'new' column:")
print(df)

# Delete the 'new' column permanently
df.drop('new', axis=1, inplace=True)
print("\nDataFrame after deleting 'new' column:")
print(df)

# Step 5: Select specific rows
print("\nRows r2, r1, r3:")
print(df.loc[['r2', 'r1', 'r3']])

# Step 6: Filter the DataFrame based on conditions
# Subset where c1 < 50
print("\nSubset where c1 < 50:")
print(df[df['c1'] < 50])

# Subset where c3 == 38 and c8 == 33
print("\nSubset where c3 == 38 and c8 == 33:")
print(df[(df['c3'] == 38) & (df['c8'] == 33)])

# Step 7: Create a DataFrame with missing data
data_dic = {
    'M': [1, 2, np.nan, 4, np.nan],
    'N': [11, 12, 13, 14, 15],
    'O': [np.nan, np.nan, np.nan, np.nan, np.nan],
    'P': [16, np.nan, 18, 19, 20]
}
df_missing = pd.DataFrame(data_dic)
print("\nDataFrame with missing data:")
print(df_missing)

# Step 8: Check for missing data
print("\nMissing data count in each column:")
print(df_missing.isnull().sum())

# Step 9: Handle missing data
# Fill missing values with 'N'
df_filled_with_n = df_missing.fillna('N')
print("\nDataFrame after filling missing values with 'N':")
print(df_filled_with_n)

# Fill missing values in column 'M' with its mean
df_filled_with_mean = df_missing.copy()
df_filled_with_mean['M'] = df_filled_with_mean['M'].fillna(df_filled_with_mean['M'].mean())
print("\nDataFrame after filling missing values in 'M' with its mean:")
print(df_filled_with_mean)

# Forward fill missing values
df_forward_filled = df_missing.fillna(method='ffill')
print("\nDataFrame after forward fill:")
print(df_forward_filled)
