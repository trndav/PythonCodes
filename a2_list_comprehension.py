import sys

x = [i for i in range(20)] # For larger lists takes less memory than Y
y = [0, 1, 2, 3]
print(x)

print("x size:", sys.getsizeof(x))
print("y size:", sys.getsizeof(y))

a = [[n for n in range(5)] for i in range(6)]
print(a)
print("a size:", sys.getsizeof(a))

b = [i for i in range(40) if i % 2 == 0]
print(b)
print("b size:", sys.getsizeof(b))