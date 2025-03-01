
# Step by steb debug - continue with continue
# Type n (next step)
# Type p a (print value of a)
# Type q (quit debugger)

import pdb

def multiply(a, b):
    pdb.set_trace()  # Pause execution here
    return a * b
#print(multiply(3, 4))

 
import logging

logging.basicConfig(level=logging.DEBUG)

def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    return a / b if b != 0 else "Cannot divide by zero"

print(divide(10, 2))
print(divide(5, 0))

