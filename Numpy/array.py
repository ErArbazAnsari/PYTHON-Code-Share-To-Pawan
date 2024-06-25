import numpy as np

# arr1 = np.array([1,2,3,4,5])
# print(arr1)

# arr2 = np.array([[1,2,3,4,5], [1,2,3,4,5]])
# print("2D Array: \n",arr2)

# arr3 = np.zeros((3,10))
# print("Zeros Array: ", arr3)

# random_array = np.random.randint((3,3))
# print("Random Array: ", random_array)

arr10 = [1, 2, 3, 4, 25]
# result = []
# for i in arr10:
#     result = result.append(arr10 + 10)
# print("Array 1: ", result)
result = np.square(arr10)

print(result)
mat = np.array([[1, 2], [3, 4]])
inv_mat = np.linalg.inv(mat)
print("Inverse Matrix: \n", inv_mat)

eig_vals, eig_vecs = np.linalg.eig(mat)
print("Eigen Values: \n", eig_vals)
