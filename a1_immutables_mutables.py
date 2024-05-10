# Immutables: str, int, bool, float, bytes, tuple
# Mutables: list, dict, set

# x = (1, 2)
# # x[0] = 1 # TypeError: 'tuple' object does not support item assignment
# y = x 
# x = (1, 2, 3)
# print(x, y)

def get_largest(number, n):
    number.sort()
    return number[-n:]

nums = [ 2, 5, 63, 7, 76, 232, 775, 21]

print(nums)
largest = get_largest(nums, 3)
print(nums)
print(largest)