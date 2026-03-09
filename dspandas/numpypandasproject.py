import pandas as pd
import numpy as np

df = pd.read_csv("covid_data.csv")

print("HEAD")
print(df.head())

print("\nTAIL")
print(df.tail())

print("\nINFO")
df.info()

print("\nDESCRIBE")
print(df.describe())

print("\nShape:", df.shape)

print("\nColumns:", df.columns)

print("\nMissing values")
print(df.isnull().sum())

df["Date"] = pd.to_datetime(df["Date"])

df["Death_Rate"] = (df["Deaths"] / df["Confirmed"]) * 100

df["Risk_Level"] = df["Confirmed"].apply(
    lambda x: "High" if x > 1000000 else "Medium" if x > 100000 else "Low"
)

india = df[df["Country/Region"] == "India"]
print("\nIndia data")
print(india.head())

high_cases = df[df["Confirmed"] > 1000000]
print("\nHigh cases")
print(high_cases.head())

print("\nRows 20–30")
print(df.iloc[20:30])

print("\nSelected columns")
print(df[["Country/Region","Confirmed","Deaths"]].head())

sorted_cases = df.sort_values(by="Confirmed", ascending=False)
print("\nTop 5 cases")
print(sorted_cases.head())

print("\nCountry count")
print(df["Country/Region"].value_counts().head())

group_country = df.groupby("Country/Region")["Confirmed"].max()
print("\nMax confirmed by country")
print(group_country.head())

group_stats = df.groupby("Country/Region").agg({
    "Confirmed": "max",
    "Deaths": "max",
    "Recovered": "max"
})
print("\nCountry statistics")
print(group_stats.head())

print("\nTotal confirmed:", df["Confirmed"].sum())
print("Average confirmed:", df["Confirmed"].mean())
print("Max confirmed:", df["Confirmed"].max())
print("Min confirmed:", df["Confirmed"].min())

# -----------------------
# NUMPY OPERATIONS
# -----------------------

cases = df["Confirmed"].values

print("\nNumPy mean:", np.mean(cases))
print("NumPy median:", np.median(cases))
print("NumPy std:", np.std(cases))
print("NumPy variance:", np.var(cases))

print("90th percentile:", np.percentile(cases,90))

print("NumPy max:", np.max(cases))
print("NumPy min:", np.min(cases))

print("Index of max case:", np.argmax(cases))

normalized = (cases - np.min(cases)) / (np.max(cases) - np.min(cases))
print("Normalized sample:", normalized[:5])

print("Square root sample:", np.sqrt(cases[:5]))
print("Log sample:", np.log(cases[:5]))