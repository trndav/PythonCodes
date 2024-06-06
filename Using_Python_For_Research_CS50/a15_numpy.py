import numpy as np

zero_vector = np.zeros(5)
one_vector = np.ones(4)
zero_matrix = np.zeros((5,3))
zero_empty = np.empty(5)

print(zero_vector)
print(one_vector)
print(zero_matrix)
print(zero_empty)


x = np.array([1,2,3])
y = np.array([4,5,6])

print(x, y)

A = np.array([[12, 13, 14], [22, 23, 25]])
print("A is:\n", A)
T = A.transpose()
print("Transpose A is:\n", T)
