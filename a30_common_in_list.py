# Common ints in list

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]

# def common(x, y):
#     common_int = []
#     for i in x:
#         if i in y:
#             common_int.append(i)
#     return common_int
# print(common(a, b))

def common(x, y):
    common_int = [i for i in y if i in x]
    return common_int
print(common(a, b))