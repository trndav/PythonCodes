# Lambda

double = lambda x: x*2
print(double(5))

add = lambda a, b: a + b 
print(add(5, 3))

is_even = lambda x: x % 2 == 0
print(is_even(3))
print(is_even(6))

pairs = [(1, 3), (4, 1), (2, 2)]
pairs.sort(key=lambda x: x[1])
print(pairs)

counter = lambda x: len(x)
print(counter("text"))

numbers = [1, 6, 3, 8, 4, 10]
filte = list(filter(lambda x: x > 5, numbers))
print(filte)

list1 = [1, 2, 3, 4, 5]
square = map(lambda x: x**2, list1)
print(list(square))

combine = lambda x, y: x + " " + y
print(combine("Hello", "World"))

words = ["banana", "apple", "cherry", "date"]
last_char_sort = sorted(words, key=lambda x: x[-1])
print(last_char_sort)

words = ["banana", "apple", "cherry", "date"]
words.sort(key=lambda x: x[-1])
print(words)