import numpy as np

# Get user input
size = int(input("Enter a number up to 10: "))
size = min(size, 10)  # Ensure it does not exceed 10

# Create an empty table filled with '.'
table = np.full((size, size), '.')
#print(table)

# Calculate number of 'X' to place (1/4 of total squares)
num_x = (size * size) // 4  

# Randomly select positions for 'X'
indices = np.random.choice(size * size, num_x, replace=False)
#print("indices: \n", indices)

# Fill those positions with 'X'
for index in indices:
    row, col = divmod(index, size)
    #print(f"row: {row}, col: {col}")
    table[row, col] = 'X'
#print(f"table: {table}")

# Find available positions (where '.')
available_positions = [(r, c) for r in range(size) for c in range(size) if table[r, c] == '.']
print("available pos:", available_positions)

# Randomly assign 'S' and 'F' to available positions
s_pos, f_pos = np.random.choice(len(available_positions), 2, replace=False)
s_row, s_col = available_positions[s_pos]
f_row, f_col = available_positions[f_pos]

table[s_row, s_col] = 'S'
table[f_row, f_col] = 'F'

# Print the table
for row in table:
    print(" ".join(row))
