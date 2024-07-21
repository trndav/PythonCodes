# map = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }

# x = 'b'
# y = map[x]

# print(f'{x} -> {y}')
# print(x, y)


# def atuple(a, b):
#     return (a, b)
# result = atuple(3,5)
# print(result)

# from typing import Tuple
# def create_tuple(a: int, b: int) -> Tuple[int, int]:
#     return (a, b)
# result = create_tuple(1, 2)
# print(result) 

# a = 3
# b = a
# print(b - 1)


# import copy # Copies are used for nested objects, like list within list
# q = [1,[2]]
# w = copy.copy(q)
# z = copy.deepcopy(q)
# print("q is w", q is w)
# print("q is z", q is z)
# print("q == z", q == z)
# print("q == w", q == w, q)
# q.append(8)
# q[1].append(23)
# print("q is", q)
# print("w is", w)
# print("z is", z)


# address_count = {'F': 1, 'o': 93, 'u': 21}
# print(max(address_count.values()))


# a = [1,2,3]
# b = ["a", "b", "c"]
# print(list(zip(a,b)))
# for x in zip(a,b):
#     print(x)


# import numpy as np
# w1 = np.random.choice(10)
# print(w1)


# print("**"*20)


# import random
# print(random.choice(["H", "T"]))


# import numpy as np
# def create_board():
#     return np.zeros((3, 3), dtype=int)
# def place(board, player, position):
#     if board[position] == 0:
#         board[position] = player
#     return board
# board = create_board()
# board = place(board, 1, (0, 0))
# print(board)


# board = np.array([[0, 1, 2],
#                   [3, 4, 5],
#                   [6, 7, 8]])
# (row_indices, col_indices) = np.where(board == 0)
# print(row_indices)  # Output: [0 1 2]
# print(col_indices)  # Output: [0 1 2]

# print(board.shape[1])


# import numpy as np
# import random 



# # Create 3x3 board for tic tac
# def create_board():
#     return np.zeros((3,3), dtype=int)
# def place(board, player, position):
#     if board[position] == 0:
#         board[position] = player
#     return board
# board = create_board()
# board[0, 0] = 1
# def possibilities(board):
#     return list(zip(*np.where(board == 0)))
# random.seed(1)
# def random_place(board, player):
#     available_position = possibilities(board)
#     if available_position:
#         choice = random.choice(available_position)
#         board[choice] = player        
#         print("Choice:", choice)
#     return board
# print(possibilities(board))
# random_place(board, 2)

# print("*"*20)

# random.seed(1)
# board = create_board()
# def random_place(board, player):
#     available_position = possibilities(board)
#     if available_position:
#         choice = random.choice(available_position)
#         print("Choice", choice)
#         board[choice] = player
#     return board
# random_place(board, 1)
# random_place(board, 2)
# random_place(board, 1)
# random_place(board, 2)
# random_place(board, 1)
# random_place(board, 2)


# def row_win(board, player):
#     for row in board:
#         if np.all(row == player):
#             return True
#     return False
# print(row_win(board, 1))


# def col_win(board, player):
#     for col in range(board.shape[1]):
#         if np.all(board[:, col] == player): # Select all rows (:) for col
#             return True
#     return False
# print(col_win(board, 1))


# board[1,1] = 2
# def diag_win(board, player):
#     # if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player): # np.diag returns the diagonal of the array, flippr - reversed
#     #     return True
#     # else:
#     #     return False
#     if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or (board[2][0] == player and board[1][1] == player and board[0][2] == player):
#         return True
#     return False
# print(diag_win(board, 2))


# def evaluate(board):
#     print(board)
#     winner = 0
#     for player in [1, 2]:
#         if row_win(board, player) or col_win(board, player) or diag_win(board, player):
#             winner = player
#     if np.all(board != 0) and winner == 0:  # Check for a draw only if the board is fully filled
#         return -1
#     return winner
# print(evaluate(board))

# num = [1, 2, 3, 4, 5]
# for x in num:
#     print("x is:", x)
#     pos = (x + 1) % 3
#     print("x + 1 mod is:", pos)


# def encode_message(message):
#     encoded_message = []
#     message = message.lower()
#     for char in message:
#         current_position = positions[char]
#         new_position = (current_position + 1) % 27
#         new_char = alphabet[new_position]

#         #if current_position == 26:
#         #    new_position = 0  # Wrap around to space ' '
#         #else:
#         #   new_position = current_position + 1
        
#         encoded_message.append(new_char)
#     return ''.join(encoded_message)

# # Example usage
# message = "In this exercise we will encode a message with a Caesar cipher"
# encoded_message = encode_message(message)
# print(encoded_message)


# import os
# entries = os.listdir()
# print(entries)


test = ["Bob", "Alan", "Grunf"]
print(list(enumerate(test)))
for index, value in enumerate(test):
    print(index, value )

import pandas as pd
data = pd.Series([1,2,3,4])
data = data.iloc[[3,0,1,2]]
data = data.reset_index(drop=True)
print(data[0])


