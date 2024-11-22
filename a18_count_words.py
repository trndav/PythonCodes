# Count words

def count_words():
    x = input("Type some sentence:\n")
    x = x.split()
    return len(x) 

print(count_words())