# Read write
# use with and create functions

# a = int(input("Type 1 if you want to write to file, or type 2 if you want to read from file: "))

# if a == 1:
#     file = open("a12_example.txt", "a")
#     b = input("Write something for file: ")
#     file.write(b + "\n")
#     file.close()

# elif a == 2:
#     filer = open("a12_example.txt", "r")
#     x = filer.read()
#     print(x)
#     filer.close()


# With and functions

def file_append(a):
    with open("a12_example.txt", "a") as file:
        b = input("Write something for file: ")
        file.write(b + "\n")

def file_read():
    with open("a12_example.txt", "r") as file:
        x = file.read()
        print(x)

def main():
    while True: 
        try:
            a = int(input("Type 1 if you want to write to file, or type 2 if you want to read from file: "))
            if a == 1:
                file_append(a)
            elif a == 2:
                file_read()
            else:
                print("Input is wrong. Try 1 or 2.")
            
        except ValueError:
            print("Input must be integer, number.")
main()