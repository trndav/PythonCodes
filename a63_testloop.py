# Loop

# Pyramid one sided
for x in range(1, 4):
    print("x"*x)

# Square
def size(a):
    for x in range(a):
        print("x"*a)
size(2)

# Generate all the possible coordinates (x, y) in a grid, where x is from 1 to 5 
# and y is from 1 to 5. However, only include those coordinates where the 
# sum of x and y is an odd number.

coordinates = []
for x in range(1, 4):
    for y in range(1, 4):
        if (x + y) % 2 != 0:
            coordinates.append((x, y))
print(coordinates)
for x in coordinates:
    print(x)

# Write a program to generate a multiplication table from 1 to 5 using nested loops.
for x in range(1, 5):
    for y in range(1, 5):
        print((x * y), end="  ")
    print()