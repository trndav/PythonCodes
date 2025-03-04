import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# 2D array (Matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Array of zeros
zeros = np.zeros((2, 3))
print(zeros)

# Array of ones
ones = np.ones((3, 3))
print(ones)

#

arr = np.array([10, 20, 30, 40])

print(arr + 5)  # Add 5 to every element
print(arr * 2)  # Multiply every element by 2
print(arr / 10) # Divide every element by 10

# Sum, mean, max, min
print(np.sum(arr), np.mean(arr), np.max(arr), np.min(arr))

#

# Reshaping an array
matrix = np.arange(1, 10).reshape(3, 3) #[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# Accessing elements
print(matrix[0, 1])  # First row, second column
print(matrix[:, 1])   # All rows, second column
print(matrix[1, :])   # Second row, all columns

#

# Random numbers between 0 and 1
rand_nums = np.random.rand(5)
print(rand_nums)

# Random integers between 1 and 10
rand_ints = np.random.randint(1, 10, (3, 3))
print(rand_ints)

# Normal distribution (mean=0, std=1)
rand_norm = np.random.randn(5)
print(rand_norm)

# 

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)
print(C)
# (1×5)+(2×7)=5+14=19
# (1×6)+(2×8)=6+16=22
# (3×5)+(4×7)=15+28=43
# (3×6)+(4×8)=18+32=50

# Transpose
print(A.T)

# Inverse (only for square matrices)
A_inv = np.linalg.inv(A)
print(A_inv)
