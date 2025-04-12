class MyContext:
    def __enter__(self):
        print("Entering the block")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the block")

with MyContext():
    print("Inside the block")