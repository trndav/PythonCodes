# Count each char

def count_chars():
    x = input("Type something, I will count each char:\n")
    a = {}
    for i in x:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    print(a)
count_chars()