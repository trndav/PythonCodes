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

# BFS to find path from 'S' to 'F'
def bfs(table, start, end, size):
    queue = [start]
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    while queue:
        row, col = queue.pop(0)  # Remove first element (FIFO)

        if (row, col) == end:
            print(f"Path found! Path: {visited}")
            for row in table:
                print(" ".join(row))
            return True  # Reached 'F'
        
        if (row, col) in visited:
            continue
        
        visited.add((row, col))

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < size and 0 <= new_col < size and table[new_row][new_col] in {'.', 'F'}:
                queue.append((new_row, new_col))
    
    print("No path found!")
    return False  # No path exists

# Run BFS to check if 'S' can reach 'F'
bfs(table, (s_row, s_col), (f_row, f_col), size)