# size = 5
# fill_ratio = 0.30

# def generate_board(size, fill_ratio):
#     board = [['.' for _ in range(size)] for _ in range(size)]
#     return board
# print(generate_board(size, fill_ratio))


def is_palindrome(x):
    x = x.replace(" ", "").lower()
    b = x[::-1].lower().replace(" ", "")
    if x == b:
        print(True)

is_palindrome("Never odd or even") #→ True

#a = "bom"
# print(a[::-1])