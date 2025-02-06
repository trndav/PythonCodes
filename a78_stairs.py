# Stairs test

imp = int(input("Enter number up to 10:\n"))

for x in range(imp, 0, -1):
    print("X"*x)

for x in range(1, imp):
    print("X"*x)

for i in range(1, imp + 1):
    print(" " * (imp - i) + "X" * i)