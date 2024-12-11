# Leap year

def leap():
    x = int(input("Enter a year:\n"))
    if (x % 4 == 0 and x % 100 == 0) or (x % 400 == 0):
        return f"{x} is leap year."
    else:
        return f"{x} is not leap year."


print(leap())