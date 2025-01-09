def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments received: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorator_with_args
def greet(name, message):
    print(f"{name}: {message}")

# Call the decorated function with arguments
greet("Alice", "Hello, world!")
