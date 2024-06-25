import matplotlib.pyplot as plt

x = ['cse1', 'cse2', 'cse3', 'cse4', 'cse5']
y = [10, 20, 30, 40, 5]
# plt.plot(x,y)
# plt.scatter(x,y)
plt.plot(x, y, label='CSE DATA', color='red', marker='o', markersize=10, linestyle='--', linewidth=2)
plt.legend()
plt.title("Arbaz Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig('5.png')
plt.show()
