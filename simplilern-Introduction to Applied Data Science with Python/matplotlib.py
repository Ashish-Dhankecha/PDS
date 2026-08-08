import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)
plt.show()

plt.plot(x, y, color="red")
plt.title("Simple Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

names = ["A", "B", "C", "D", "E"]
marks = [80, 65, 90, 70, 85]

plt.bar(names, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.bar(names, marks, color="green")
plt.show()

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

marks = [45, 50, 55, 60, 65, 70, 70, 75, 80, 85, 90, 95]

plt.hist(marks, bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of students")
plt.show()

plt.pie(marks[:5], labels=names, autopct="%1.1f%%")
plt.show()

x = np.arange(1, 6)
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

plt.plot(x, y1, label="data 1")
plt.plot(x, y2, label="data 2")

plt.legend()
plt.show()

plt.figure(figsize=(8, 5))

plt.subplot(2, 2, 1)
plt.plot(x, y1)

plt.subplot(2, 2, 2)
plt.bar(x, y1)

plt.subplot(2, 2, 3)
plt.scatter(x, y1)

plt.subplot(2, 2, 4)
plt.hist(y1)

plt.show()

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker="o", linestyle="--", color="blue")

plt.title("My Graph")
plt.xlabel("Input")
plt.ylabel("Output")

plt.grid()

plt.show()

plt.savefig("graph.png")