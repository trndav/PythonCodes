size = 5
fill_ratio = 0.30

def generate_board(size, fill_ratio):
    board = [['.' for _ in range(size)] for _ in range(size)]
    return board
print(generate_board(size, fill_ratio))