# return gives back a value and ends the function.
# yield gives back a value but keeps the function alive

def count_up_to(n):
    count = 1
    while count <= n:
        yield count        
        count += 1

for num in count_up_to(5):
    print(num)
