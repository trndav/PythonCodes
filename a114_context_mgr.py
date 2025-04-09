# __enter__ and __exit__

class MyContext:
    def __enter__(self):
        print("Entering context")
        return "Some resource"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        if exc_type:
            print(f"An error occurred: {exc_val}")
        return True  # suppress exceptions if needed

with MyContext() as resource:
    print(f"Using: {resource}")
    # raise ValueError("Oops")  # Uncomment to test error handling
