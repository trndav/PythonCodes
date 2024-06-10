import time
import random
import numpy as np

start_time = time.perf_counter()
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Time passed is: {elapsed_time:.9f}")


# start_time = time.perf_counter()
# time.sleep(1)
# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f"Time passed is: {elapsed_time:.9f} seconds")


start_time = time.perf_counter()
ys = []
for rep in range(100000):
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x 
    ys.append(y)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Time passed is: {elapsed_time:.9f}")


# Same operation with numpy - much faster
start_time = time.perf_counter()
X = np.random.randint(1, 7, (100000, 10))
Y = np.sum(X, axis=1)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Time passed is: {elapsed_time:.9f}")

print(type(elapsed_time))