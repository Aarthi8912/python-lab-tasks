
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Student Data Analysis App")

df = pd.read_csv("streamlitadd/data.csv")

st.subheader("Dataset")
st.write(df)

df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

st.subheader("Dataset with Total & Average")
st.write(df)

st.subheader("Top Students")
top_students = df.sort_values(by="Total", ascending=False).head()
st.write(top_students)

st.subheader("High Average Students (>85)")
high_avg = df[df["Average"] > 85]
st.write(high_avg)

st.subheader("NumPy Statistics (Math Marks)")
math_scores = df["Math"].values

st.write("Mean:", np.mean(math_scores))
st.write("Median:", np.median(math_scores))
st.write("Standard Deviation:", np.std(math_scores))
st.write("Max:", np.max(math_scores))
st.write("Min:", np.min(math_scores))

#linechart
st.subheader("Average Marks Chart")
fig1, ax1 = plt.subplots()
ax1.plot(df["Student"], df["Average"], marker="o")
ax1.set_title("Student Average Marks")
ax1.set_xlabel("Students")
ax1.set_ylabel("Average")
plt.xticks(rotation=45)
st.pyplot(fig1)

#barchart
st.subheader("Total Marks Chart")
fig2, ax2 = plt.subplots()
ax2.bar(df["Student"], df["Total"])
ax2.set_title("Total Marks")
ax2.set_xlabel("Students")
ax2.set_ylabel("Marks")
plt.xticks(rotation=45)
st.pyplot(fig2)

#scatterplot
st.subheader("Study vs Marks")
fig3, ax3 = plt.subplots()
ax3.scatter(df["Hours_Studied"], df["Average"])
ax3.set_title("Hours Studied vs Average")
ax3.set_xlabel("Hours")
ax3.set_ylabel("Average")
st.pyplot(fig3)