# Largest number

def largest_number():
    x = input("Type a list of numbers: ").split(",")
    x = [int(num.strip()) for num in x]
    return max(x)

print(largest_number())