print("Lets test raise and error message.")

while True:
    usr = input("Type some whole number or type 'exit' to exit: \n")

    if usr == "exit":
        break

    if not usr.isdigit():
        print("You did not type a number")
        continue

    usr = int(usr)
    print(usr*usr)
    break
        
print("Now with raise.")
usr2 = input("Type another whole number or type 'exit' to exit: \n")

while usr != "exit":
    if not usr2.isdigit():
        raise ValueError("You did not type a number")
    else:
        usr2 = int(usr2)
        print(usr2*usr2)
        break