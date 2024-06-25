import numpy as np

print(np.array([10, 12, 13, 15]))
# print(np.array([1,2,3],[1,2]).shape)

# print(np.zeros((5,3)))


# print(np.ones((5))[0])

num1 = np.array((1, 2, 3, 4, 5))
num2 = np.array((5, 6, 7, 8, 9))
# print(num1 + num2)

num3 = np.array(((1, 2, 3, 4), (5, 6, 7, 8)))
print(np.array(num3).shape)

num3.reshape(4, 2)
print(num3)


print(np.random.randn(200,5))
# print(np.random.randint(1,10))

