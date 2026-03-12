
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y1 = [10,20,30,40,50]
y2 = [5,15,25,35,45]
y3 = [2,4,6,8,10]
data = [10,20,20,30,30,40,50]

plt.figure(figsize=(10,8))

# 1 Line Plot
plt.subplot(2,2,1)
plt.plot(x, y1, marker="o")
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")

# 2 Bar Chart
plt.subplot(2,2,2)
plt.bar(x, y2)
plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Value")

# 3 Scatter Plot
plt.subplot(2,2,3)
plt.scatter(x, y3)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

# 4 Histogram
plt.subplot(2,2,4)
plt.hist(data, bins=5)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("advanced_subplot.png")
plt.show()