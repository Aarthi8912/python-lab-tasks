
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y1 = [65,70,75,80,85]
y2 = [60,68,72,78,82]
plt.plot(x, y1, label="Student A", linestyle="-", marker="o")
plt.plot(x, y2, label="Student B", linestyle="--", marker="s")
plt.title("Student Marks Progress")
plt.xlabel("Tests")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.savefig("marks_progress.png")
plt.show()


import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y1 = [30,32,34,33,35]
y2 = [28,30,31,32,33]
plt.plot(x, y1, label="City A", linestyle="-.", marker="o")
plt.plot(x, y2, label="City B", linestyle=":", marker="d")
plt.title("Temperature Comparison")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.savefig("temperature_chart.png")
plt.show()


import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y1 = [100,120,150,170,200]
y2 = [90,110,140,160,180]
plt.plot(x, y1, label="Product A", linestyle="--", marker="^")
plt.plot(x, y2, label="Product B", linestyle="-", marker="s")
plt.title("Product Sales Growth")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.savefig("product_sales.png")
plt.show()