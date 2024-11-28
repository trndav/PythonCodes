# Factorial

def factorial():
    x = int(input("Enter number to calculate factorial:\n"))
    count = 1
    for i in range(1, x+1):
        count *= i
        print(f"count is: {count}, i is {i}")

    print(count)

factorial()

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# num = int(input("Enter a number: "))
# print(f"Factorial of {num} is {factorial(num)}")