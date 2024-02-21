import pandas as pd

# Read the wide format CSV file
df = pd.read_csv('Raw_Data.csv')

df = df.stack()
df.to_csv('output.csv', index=False)


