# Decorator for memoization
def memoize(func):
    cache = {}
    #print(f"Cache: {cache}")
    def wrapper(n):
        print(n)
        if n not in cache:
            cache[n] = func(n)  # Store result in cache if not already present
        return cache[n]
    return wrapper

# Expensive function
@memoize
def factorial(n):
    #print(n)
    if n == 0:
        return 1
    #print(n * factorial(n - 1))
    return n * factorial(n - 1)

# Test
print(factorial(5))  # Output: 120
print(factorial(6))  # Output: 720 (reuses result for factorial(5))
