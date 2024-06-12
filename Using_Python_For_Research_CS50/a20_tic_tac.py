import numpy as np
import random 


# random.seed(1)
# Create 3x3 board for tic tac
def create_board():
    return np.zeros((3,3), dtype=int)


# 
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    return board


# Return empty positions on board
def possibilities(board):
    return list(zip(*np.where(board == 0)))


def random_place(board, player):
    available_position = possibilities(board)
    if available_position:
        choice = random.choice(available_position)
        board[choice] = player
    return board


def row_win(board, player):
    #     if np.any(np.all(board==player, axis=1)): # this checks if any row contains all positions equal to player.
    #     return True
    # else:
    #     return False
    for row in board:
        if np.all(row == player):
            return True
    return False


def col_win(board, player):
    # if np.any(np.all(board==player, axis=0)):
    #     return True 
    # else:
    #     return False    
    for col in range(board.shape[1]):
        if np.all(board[:, col] == player): # Select all rows (:) for col
            return True
    return False


def diag_win(board, player):
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or (board[2][0] == player and board[1][1] == player and board[0][2] == player):
        return True
    return False


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:  # Check for a draw only if the board is fully filled
        winner = -1
    return winner


# def play_game():
#     board = create_board()
#     current_player = 1

#     while True:
#         board = random_place(board, current_player)
#         result = evaluate(board)
#         if result != 0:
#             return result
#         current_player = 2 if current_player == 1 else 1

# results = []
# for _ in range(10):    
#     result = play_game()
#     results.append(result)

# print("Results of games:")
# print(results)
# print(results.count(1), "times player 1 won.")

random.seed(1) 
def play_strategic_game():
    board = create_board()
    board = place(board, 1, (1, 1))
    current_player = 2

    while True:
        board = random_place(board, current_player)
        result = evaluate(board)
        if result != 0:
            return result
        current_player = 2 if current_player == 1 else 1
play_strategic_game()

results = []
for _ in range(1000):    
    result = play_strategic_game()
    results.append(result)

# print("Results of games:")
# print(results)
print(results.count(1), "times player 1 won.")