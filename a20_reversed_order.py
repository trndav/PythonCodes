# Reversed order

def reversed():
    x = input("Type some sentence which we will reverse:\n")
    reversed_sentence = " ".join(x.split()[::-1])
    print(reversed_sentence)

reversed()
