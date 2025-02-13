import time

def slow_function(n):
    time.sleep(2)  # Simulate a slow operation
    return n * n

print("Slow function")
print(slow_function(4))  # Takes 2 seconds
print(slow_function(4))  # Takes 2 seconds again (no caching)


from functools import lru_cache

@lru_cache(maxsize=None)  # Cache unlimited results
def fast_function(n):
    time.sleep(2)  # Simulate a slow operation
    return n * n

print("Cached fast function")
print(fast_function(5))  # Takes 2 seconds
print(fast_function(5))  # Instant! Returns cached result
