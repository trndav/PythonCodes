# Reversed

usr = input("Type something nice: \n")


with open("a69.txt", "a") as file:
    file.write(usr[::-1]+"\n")


x = open("a69.txt", "r")
for line in x:
    print(line)