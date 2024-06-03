
# x = [2, 4, 6, 8]
# print(x[0])
# print(x[-1])

# x.append(16)
# print(x)

# y = [10, 12, 14]

# sum = x + y
# print(sum)

# # Reverse
# print(x[::-1])
# print(x.reverse()) # Reverse in place method - None to print
# print(x)

# names = ["Bob", "Bumerang", "Ana", "Tron", "Rock"]
# print(names)
# print(names.sort())
# names.sort()
# print(names)

# names.reverse()
# print(names)
# print("Sortirana lista:", sorted(names)) # Sorted - new list
# print(names)

# print(len(names))


numbers = range(10)
squares = []
for i in numbers:
    squares.append(i**2)
print(squares)


trip = [number*3 for number in numbers]
print(trip)

# for x in range(10):
#     if x % 2 == 0:
#         print(x)

j = sum([x for x in range(10) if x % 2 != 0])
print(j)
