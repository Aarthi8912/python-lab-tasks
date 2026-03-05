import pandas as pd
import numpy as np

data = {
    "Name": ["ARUN", "PRIYA", "KAVYA", "ARUN", None],
    "Math": [78, 85, None, 78, 90],
    "Science": [88, None, 92, 88, 95],
    "English": [75, 80, 85, 75, None],
    "Department": ["CSE", "IT", "CSE", "CSE", "ECE"]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)


df["Math"] = df["Math"].fillna(df["Math"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())
df["English"] = df["English"].fillna(df["English"].mean())

print("\nAfter fillna")
print(df)

df = df.dropna(subset=["Name"])

print("\nAfter dropna (remove missing names)")
print(df)

df = df.rename(columns={"Math": "Math_Marks"})

print("\nAfter rename column")
print(df)

df["Math_Marks"] = df["Math_Marks"].astype(int)

print("\nAfter astype conversion")
print(df.dtypes)

sorted_df = df.sort_values(by="Math_Marks")

print("\nSorted by Math Marks")
print(sorted_df)

cond_sort = df[df["Math_Marks"] > 80].sort_values(by="Science")

print("\nConditional Sort (Math > 80)")
print(cond_sort)

df["Total"] = df[["Math_Marks", "Science", "English"]].apply(lambda x: x.sum(), axis=1)

print("\nAfter Apply Lambda (Total Marks)")
print(df)

print("\nDuplicate Rows")
print(df[df.duplicated()])

df["Name"] = df["Name"].str.lower()

print("\nNames converted to lowercase")
print(df)

cse_students = df[df["Department"].str.contains("CSE")]

print("\nStudents from CSE Department")
print(cse_students)