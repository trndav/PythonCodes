import time

def sum_numbers():
    total = 0
    for i in range(1, 1000001):
        total += i
        if total % 1000 == 0:
            print(total)
    return total

start_time = time.time()  # start time
sum_numbers()  
end_time = time.time()  # end time

print("Execution Time:", end_time - start_time, "seconds")
