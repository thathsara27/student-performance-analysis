import pandas as pd

df = pd.read_csv('StudentPerformanceFactors.csv')

print(df.shape)
print(df.isnull().sum())
print(df.describe())