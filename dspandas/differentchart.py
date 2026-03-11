
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [5,10,15,20,25]
plt.plot(x, y, marker="o", label="Growth")
plt.title("Simple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)
plt.savefig("line_plot.png")
plt.show()



import matplotlib.pyplot as plt
categories = ["A","B","C","D"]
values = [10,20,15,25]
plt.bar(categories, values)
plt.title("Bar Chart ")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.savefig("bar_chart.png")
plt.show()



import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.scatter(x, y)
plt.title("Scatter Plot ")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.savefig("scatter_plot.png")
plt.show()


import matplotlib.pyplot as plt
data = [10,20,20,30,30,30,40,40,50]
plt.hist(data, bins=5)
plt.title("Histogram ")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()


import matplotlib.pyplot as plt
labels = ["Python","Java","C++","JavaScript"]
sizes = [40,25,20,15]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Programming Language Popularity")
plt.savefig("pie_chart.png")
plt.show()