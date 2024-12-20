# Decorator

def log_call(func):
    def wrapper(*args, **kwargs):
        # Print the name of the function and its arguments
        print(f"Function '{func.__name__}' was called with arguments: {args} and keyword arguments: {kwargs}")
        # Call the original function and store its result
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

@log_call
def greet(name, age=None):
    return f"Hello, {name}! Age: {age}"

#add(3, 5)
print(add(3, 5))

#greet(name="Alice", age=30)
print(greet(name="Alice", age=30))

