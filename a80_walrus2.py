# Walrus in list comprehension
a = [10, 20, 30, 40, 50, 60, 70]

b = [x for num in a if (x := num * 2) > 50]
print(b)

# Test
b2 = [x for x in a if x*2 > 50]
print(b2)

# Without Walrus
b3 = [x*2 for x in a if x*2 > 50]
print(b3)

# Avoids calling readline() twice
with open("a69.txt") as file:
    while (line := file.readline().strip()):
        print(f"Processing: {line}")
