# def simple_decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()  # Call the original function
#         print("After the function runs")
#     return wrapper

# @simple_decorator
# def my_function():
#     print("This is the actual function")

# my_function()



# def log_arguments(func):
#     def wrapper(*args, **kwargs):
#         print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
#         result = func(*args, **kwargs) 
#         return result
#     return wrapper

# @log_arguments
# def greet(name, age):
#     print(f"Hello, my name is {name} and I am {age} years old!")

# # Call the function
# greet("Alice", 30)



def ensure_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError(f"Negative value detected: {arg}")
        print("All arguments are positive!")
        return func(*args, **kwargs)
    return wrapper

@ensure_positive
def add_numbers(a, b):
    return a + b

try:
    result = add_numbers(5, 3)
    print(f"Result: {result}")
    
    result = add_numbers(5, -2)
except ValueError as e:
    print(e)

print(add_numbers(4, 2))
print(add_numbers(4, -2))