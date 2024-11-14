# Read write
# use with and create functions

a = int(input("Type 1 if you want to write to file, or type 2 if you want to read from file: "))

if a == 1:
    file = open("a12_example.txt", "a")
    b = input("Write something for file: ")
    file.write(b + "\n")
    file.close()

elif a == 2:
    filer = open("a12_example.txt", "r")
    x = filer.read()
    print(x)
    filer.close()

