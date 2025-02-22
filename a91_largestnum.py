import time

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num 
    return max_num 

nums = [10, 20, 3, 66, 4, 18, 33, 89, 121, 99]
start_time = time.time()
print(find_max(nums))
end_time = time.time()

print(f"Time running: {end_time - start_time:.7f}.")