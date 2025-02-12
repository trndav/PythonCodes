from itertools import groupby

numbers = [1, 1, 2, 2, 2, 3, 3, 4, 1, 1]
numbers.sort()
grouped = {key: list(group) for key, group in groupby(numbers)}

print(grouped)


words = ["apple", "apricot", "banana", "berry", "cherry", "cranberry", "avocado"]
words.sort()  # `groupby()` requires sorted data
grouped = {key: list(group) for key, group in groupby(words, key=lambda x: x[0])}

print(grouped)
