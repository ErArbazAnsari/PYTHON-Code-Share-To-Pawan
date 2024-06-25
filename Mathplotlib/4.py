import matplotlib.pyplot as plt

section = ["CSE-1", "CSE-2", "CSE-3", "CSE-4"]
students = [600, 70, 80, 90]
plt.pie(students, labels=section, autopct='%1.1f%%')
plt.show()