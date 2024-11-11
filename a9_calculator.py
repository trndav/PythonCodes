# Simple calculator app

a = int(input("Type first number: "))
b = int(input("Type second number: "))
c = input("Type * for multiply, / to divide, + to sum or - to substract: ")

try: 
    if c == "*":
        print(a * b)

    elif c == "/":
        if b != 0:
            print(f"Result: {a / b}")
        else:
            print("Error: Division by zero is not allowed.")

    elif c == "+":
        print(a + b)

    elif c == "-":
        print(a - b)

    else:
        print("Invalid operation.")
except ValueError:
    print("Error: Invalid numbers.")