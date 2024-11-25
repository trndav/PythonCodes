# List comprehensions

squares = [x**2 for x in range(10)]
print(squares)

result = [x for x in range(10) if x % 2 == 0]
print(result)

words = ["hola", "hail", "wazaap"]
uppercase = [word.upper() for word in words]
print(uppercase)

even = [x for x in range(10) if x % 2 != 0]
print(even)