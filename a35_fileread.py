# File read

filename = input("Enter name of file to open:\n")

while True:
    try: 
        with open(filename, "r") as file:    
            content = file.read()
            print(content)
            break

    except FileNotFoundError:
        print("File was not found.")
        filename = input("Enter name of file to open:\n")