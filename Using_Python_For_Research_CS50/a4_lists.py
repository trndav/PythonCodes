
x = [2, 4, 6, 8]
print(x[0])
print(x[-1])

x.append(16)
print(x)

y = [10, 12, 14]

sum = x + y
print(sum)

# Reverse
print(x[::-1])
print(x.reverse()) # Reverse in place method - None to print
print(x)

names = ["Bob", "Bumerang", "Ana", "Tron", "Rock"]
print(names)
print(names.sort())
names.sort()
print(names)

names.reverse()
print(names)
print("Sortirana lista:", sorted(names)) # Sorted - new list
print(names)

print(len(names))