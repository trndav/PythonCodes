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
print("Transpose T is:\n", T)

B = np.array(np.zeros(5))
print(B)

print("*"*20)

q = np.array([1,2,3])
w = np.array([4,5,6])
E = np.array([[11,12,13], [22,32,34]])
R = np.array([[44,55,66], [77,88,99]])

print("q[1:2]: ", q[:2])
print("x+y", x + y)
print("E[1]", E[1])
print("E[:1]", E[:1])
print("E[:2]", E[:2])
print("E[:,1]", E[:,1]) # first column
print("E[:,2]", E[:,2])
print("E[:,2]+E[:,1]", E[:,2]+E[:,1])
print("E[1,:]", E[1,:])
print("E[1,:] + R[1,:]", E[1,:] + R[1,:])


# a = np.array([1,2])
# b = np.array([3,4,5])
# c = a + b
# print(c)


print("*"*20)


z1 = np.array([1,3,5,7,9])
z2 = z1 + 1
print(z2)
ind = [0, 1, 2]
print(z1[ind]) # ind - index of z1
ind2 = np.array([2,3,4])
print(z1[ind2])
print("z1 > 6:", z1 > 6)


print(z1[z1 > 6])
print(z2[z2 > 6])
ind3 = z1 > 6
print(z1[ind3])


w = z1[0:3]
w[0] = 3
print(w)
print(z1)


w1 = z1[ind]
w1[0] = 4
print(w1)
print(z1)


# c = b[1:]
# b[a] is c


print(np.linspace(1, 15, 5))
print(np.logspace(1, 2, 10)) # log

print(np.logspace(np.log10(2), np.log10(500), 10))


# A = np.array([[12, 13, 14], [22, 23, 25]])
print(A.shape)
print(A.size)


u = np.random.random(10) # rand 0-1
print(u)
print(np.any(u > 0.9))
print(np.all(u >= 0.1))


o = 5
print(not np.any([o%i == 0 for i in range(2, o)])) # Primes


print("*"*20)


arr = np.ones((2,3))
arr2 = arr.copy()
print(arr2)
print(id(arr2))
arr2.resize((4,5))
print(arr2)
print(id(arr2))