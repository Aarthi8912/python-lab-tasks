import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")

print(df.head())

print(df.tail())

print(df.info())

print(df.describe())

print("\n----- TOP 5 Highest Fare -----")
print(df.sort_values(by="Fare", ascending=False).head(5))

print("\n----- TOP 50 Records -----")
print(df.head(50))

print("\n----- SUM of Numeric Columns -----")
print(df.sum(numeric_only=True))

print("\n----- MIN Values -----")
print(df.min(numeric_only=True))

print("\n----- MAX Values -----")
print(df.max(numeric_only=True))

print("\n----- COUNT of Non-Null Values -----")
print(df.count())

print("\n----- Retrieve Specific Rows (Row 10 to 20) -----")
print(df.iloc[10:21])

print("\n----- Retrieve Passengers Age > 60 -----")
print(df[df["Age"] > 60])

fare_array = df["Fare"].dropna().values

print("\n----- NumPy Operations on Fare -----")
print("Mean Fare:", np.mean(fare_array))
print("Median Fare:", np.median(fare_array))
print("Standard Deviation:", np.std(fare_array))
print("Maximum Fare:", np.max(fare_array))
print("Minimum Fare:", np.min(fare_array))