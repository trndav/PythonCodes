import numpy as np
import random 

def create_board():
    return np.zeros((3,3), dtype=int)

x = create_board()
print(x)


def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    return board

board = create_board()
board = place(board, 1, (0,0))
print(board)


def possibilities(board):
    return list(zip(*np.where(board == 0)))
print(possibilities(board))


random.seed(1)
def random_place(board, player):
    available_position = possibilities(board)
    choice = random.choice(available_position)
    board[choice] = player
    return board

place = random_place(board, 2)
print(place)


# Test 3 places each player
# random.seed(1)
# board = create_board()
# for _ in range(3):
#     random_place(board, 1)
#     random_place(board, 2)
# print(board)


# def row_win(board, player):
#     if (board[0][0] == player & board[1][0] == player & board[2][0] == player) | (board[0][1] == player & board[1][1] == player & board[2][1] == player) | (board[0][2] == player & board[1][2] == player & board[2][2] == player):
#         return True
#     return False

board = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
print(board)
# Or simpler
def row_win(board, player):
    for row in board:
        if np.all(row == player):
            print(f"Player {player} wins")
            return True
    print("No win")
    return False
row_win(board, 1)


def col_win(board, player):
    for col in range(board.shape[1]):
        if np.all(board[:, col] == player): # Select all rows (:) for col
            print(f"Player {player} wins")
            return True
    print("No win")
    return False
col_win(board, 1)
