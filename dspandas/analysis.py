import pandas as pd
import numpy as np


df = pd.read_csv("supermarket_sales.csv")

print("----- FIRST 5 ROWS -----")
print(df.head())


print("\nMissing Values")
print(df.isnull().sum())


df["Sales"] = df["Sales"].fillna(df["Sales"].mean())


df["Date"] = pd.to_datetime(df["Date"])

print("\nDataset Info")
print(df.info())


high_sales = df[df["Sales"] > 500]

print("\nHigh Sales (>500)")
print(high_sales.head())


sorted_sales = df.sort_values(by="Sales", ascending=False)

print("\nTop 5 Highest Sales")
print(sorted_sales.head())


print("\nTotal Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Maximum Sale:", df["Sales"].max())
print("Minimum Sale:", df["Sales"].min())


group_sales = df.groupby("Product line")["Sales"].sum()

print("\nTotal Sales by Product Line")
print(group_sales)

city_sales = df.groupby("City")["Sales"].mean()

print("\nAverage Sales by City")
print(city_sales)