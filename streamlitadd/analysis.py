import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print("FIRST 5 ROWS")
print(df.head())

print("\nDATA INFO")
print(df.info())

print("\nDESCRIBE")
print(df.describe())

print("\nCOLUMNS")
print(df.columns)

print("\nSHAPE:", df.shape)


df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Average"] = df["Total"] / 3

print("\nDataset with Total and Average")
print(df)

sorted_df = df.sort_values(by="Total", ascending=False)
print("\nTop Students")
print(sorted_df.head())

high_avg = df[df["Average"] > 85]
print("\nHigh Average Students")
print(high_avg)


math_scores = df["Math"].values

print("\nNumPy Mean:", np.mean(math_scores))
print("NumPy Median:", np.median(math_scores))
print("NumPy Std:", np.std(math_scores))
print("NumPy Max:", np.max(math_scores))
print("NumPy Min:", np.min(math_scores))


normalized = (math_scores - np.min(math_scores)) / (np.max(math_scores) - np.min(math_scores))
print("Normalized Math Scores:", normalized)


#linechart
plt.plot(df["Student"], df["Average"], marker="o")
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.savefig("average_marks.png")
plt.show()

#barchart
plt.bar(df["Student"], df["Total"])
plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.xticks(rotation=45)
plt.savefig("total_marks.png")
plt.show()

#scatterplot
plt.scatter(df["Hours_Studied"], df["Average"])
plt.title("Study Hours vs Average Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Average Marks")
plt.savefig("study_vs_marks.png")
plt.show()