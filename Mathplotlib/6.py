import matplotlib.pyplot as plt

x = ['cse1', 'cse2', 'cse3', 'cse4', 'cse5','cse6', 'cse7', 'cse8', 'cse9', 'cse10']
y = [10, 20, 30, 40, 5, 10, 20, 30, 40, 5]
plt.bar(x, y, label='CSE DATA', color='skyblue', width=0.5, edgecolor='red', linewidth=2)

plt.legend()
plt.grid(True)
plt.title("Arbaz Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()