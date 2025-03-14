import numpy as np

# Get user input
size = int(input("Enter a number up to 10: "))
size = min(size, 10)  # Ensure it does not exceed 10

# Create an empty table filled with '.'
table = np.full((size, size), '.')
print(table)

# Calculate number of 'X' to place (1/4 of total squares)
num_x = (size * size) // 4  

# Randomly select positions for 'X'
indices = np.random.choice(size * size, num_x, replace=False)
print("indices: \n", indices)

# Fill those positions with 'X'
for index in indices:
    row, col = divmod(index, size)
    print(f"row: {row}, col: {col}")
    table[row, col] = 'X'
print(f"table: {table}")

# Print the table
for row in table:
    print(" ".join(row))
