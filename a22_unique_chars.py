# Check unique chars

def unique_chars():
    usr = input("Type some word:\n")
    x = set()
    for i in usr:
        x.add(i)

    print(f"Unique characters are: {x}")

unique_chars()