map = {
    'a': 1,
    'b': 2,
    'c': 3
}

x = 'b'
y = map[x]

print(f'{x} -> {y}')
print(x, y)


def atuple(a, b):
    return (a, b)
result = atuple(3,5)
print(result)

from typing import Tuple
def create_tuple(a: int, b: int) -> Tuple[int, int]:
    return (a, b)
result = create_tuple(1, 2)
print(result) 

a = 3
b = a
print(b - 1)


import copy # Copies are used for nested objects, like list within list
q = [1,[2]]
w = copy.copy(q)
z = copy.deepcopy(q)
print("q is w", q is w)
print("q is z", q is z)
print("q == z", q == z)
print("q == w", q == w, q)
q.append(8)
q[1].append(23)
print("q is", q)
print("w is", w)
print("z is", z)


address_count = {'F': 1, 'o': 93, 'u': 21}
print(max(address_count.values()))


a = [1,2,3]
b = ["a", "b", "c"]
print(list(zip(a,b)))
for x in zip(a,b):
    print(x)


import numpy as np
w1 = np.random.choice(10)
print(w1)


print("**"*20)


import random
print(random.choice(["H", "T"]))


import numpy as np
def create_board():
    return np.zeros((3, 3), dtype=int)
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    return board
board = create_board()
board = place(board, 1, (0, 0))
print(board)


board = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]])
(row_indices, col_indices) = np.where(board == 0)
print(row_indices)  # Output: [0 1 2]
print(col_indices)  # Output: [0 1 2]

print(board.shape[1])