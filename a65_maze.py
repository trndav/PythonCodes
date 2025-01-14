# Maze, random 

import random

def print_board(board):
    for row in board:
        print(' '.join(row))

def generate_board(size, fill_ratio):
    board = [['.' for _ in range(size)] for _ in range(size)]
    
    num_x = int(size * size * fill_ratio)
    x_positions = random.sample([(i, j) for i in range(size) for j in range(size)], num_x)
    
    for i, j in x_positions:
        board[i][j] = 'X'
    
    return board

size = 5
fill_ratio = 0.30  # 30% of the board will be filled with 'X'
board = generate_board(size, fill_ratio)
print_board(board)
