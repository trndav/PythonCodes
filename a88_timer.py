import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        file_name = "a69.txt"
        with open(file_name, "r") as file:
            for line in file:
                print(line)
        return self  # Can be used in 'as' clause

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        print(f"Execution time: {self.end - self.start:.6f} seconds")

# Use the context manager
with Timer():
    time.sleep(2)  # Simulate a task
