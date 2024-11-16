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

# def file_append(a):
#     with open("a12_example.txt", "a") as file:
#         b = input("Write something for file: ")
#         file.write(b + "\n")

# def file_read():
#     with open("a12_example.txt", "r") as file:
#         x = file.read()
#         print(x)

# def main():
#     while True: 
#         try:
#             a = int(input("Type 1 if you want to write to file, or type 2 if you want to read from file: "))
#             if a == 1:
#                 file_append(a)
#             elif a == 2:
#                 file_read()
#             else:
#                 print("Input is wrong. Try 1 or 2.")
            
#         except ValueError:
#             print("Input must be integer, number.")
# main()


# With history log

from datetime import datetime
filename = "a12_example.txt"

def history_log(action, details=""):
    with open("a12_history_log.txt", "a") as history_file:
        timestamp = datetime.now().strftime("%H:%M:%S, %d.%m.%Y")
        history_file.write(f"{timestamp} - {action}: {details}\n")

def file_append(a):
    with open(filename, "a") as file:
        b = input("Write something for file: ")
        file.write(b + "\n")
        history_log("Write", b)

def file_read():
    with open(filename, "r") as file:
        x = file.read()
        print(x)
        history_log("Read", "Read file contents.")

def end_work():
    print("Exiting. Goodbye!")

def main():
    while True: 
        try:
            a = int(input("Type 1 if you want to write to file, type 2 if you want to read from file, or type 3 to quit: "))
            if a == 1:
                file_append(a)

            elif a == 2:
                file_read()

            elif a  == 3:
                history_log("Exit.", "User quit app.")
                end_work()
                break

            else:
                print("Input is wrong. Try 1 or 2.")
            
        except ValueError:
            print("Input must be integer, number.")
main()
