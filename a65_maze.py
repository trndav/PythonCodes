# Maze, random. Breadth-First Search (BFS) function 

import random
from collections import deque

def print_board(board):
    for row in board:
        print(' '.join(row))

def generate_board(size, fill_ratio):
    board = [['.' for _ in range(size)] for _ in range(size)]
    
    num_x = int(size * size * fill_ratio)
    x_positions = random.sample([(i, j) for i in range(size) for j in range(size)], num_x)
    
    for i, j in x_positions:
        board[i][j] = 'X'
    
    # Ensure start and end are not blocked
    board[0][0] = '.'
    board[size-1][size-1] = '.'
    
    return board

def find_path(board):
    size = len(board)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (0, 0)
    end = (size - 1, size - 1)
    visited = set()
    queue = deque([(start, [start])])  # Each item is (current_position, path_taken)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path  # Return the path when the end is reached

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None  # Return None if no path exists

# Generate the board
size = 5
fill_ratio = 0.30  # 30% of the board will be filled with 'X'
board = generate_board(size, fill_ratio)

# Print the board
print("Generated Maze:")
print_board(board)

# Find and print the path
path = find_path(board)
if path:
    print("\nThere is a path from the top-left to the bottom-right!")
    print("Path:", path)
else:
    print("\nNo path exists from the top-left to the bottom-right!")
