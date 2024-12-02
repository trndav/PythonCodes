# Second largest

x = input("Type few numbers:\n").split(" ")
a = []
for i in x:
    a.append(i)
a.sort(reverse=True)
print(a[1])

# x = input("Type a few numbers separated by spaces:\n").split()
# a = [int(i) for i in x]  # Convert to integers
# a.sort(reverse=True)
# print(f"The second largest number is: {a[1]}")