
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    x = input("Type something: \n")
    print(f"This is what you typed: {x}.")

say_hello()
