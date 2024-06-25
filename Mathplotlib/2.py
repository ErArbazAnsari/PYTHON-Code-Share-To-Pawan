import matplotlib.pyplot as plt

section = ["CSE-1", "CSE-2", "CSE-3", "CSE-4"]
students = [60, 70, 80, 90]

plt.title("Students in CSE")
plt.xlabel('X Label')

plt.ylabel('Y Label')
plt.bar(section, students)
plt.show()