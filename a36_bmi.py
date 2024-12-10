# Body Mass Index 

def bmi(weight, height):
    return weight / ((height /100) ** 2)

def category(x):
    if x <= 18.5:
        print("You are underweight.")
    elif x > 18.5 and x < 25:
        print("You are normal weight.")
    else:
        print("You are overweight.")

a = int(input("What is your weight in kg?\n"))
b = int(input("What is your height in cm?\n"))
print(bmi(a, b))

category(bmi(a, b))