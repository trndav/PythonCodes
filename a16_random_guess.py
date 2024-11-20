# Guess random number

import random

def guess_number():
    print("Welcome to the Number guessing game!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts +=1 

            if guess < secret_number:
                print(f"No, number is higher than {guess}.")
            elif guess > secret_number:
                print(f"No, number is less than {guess}.")
            else:
                print(f"You won! {guess} is secret number!")
                break
        
        except ValueError:
            print("Incorrect input. Your guess must be number between 1 and 100.")

guess_number()