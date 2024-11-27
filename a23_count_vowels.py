# Count Vowels

def count_vowels():
    x = ["a", "e", "i", "o", "u"]
    a = input("Type a word or sentence:\n").lower()
    counter = 0
    for i in a:
        if i in x:
            counter += 1
    return f"Number of vowels is: {counter}."

print(count_vowels())