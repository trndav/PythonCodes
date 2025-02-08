# Without Walrus
# x = input("Enter number or 'q': ")
# while x != "q":
#     print(f"You entered: {x}")
#     x = input("Enter number or 'q':")

# With Walrus
while (x := input("Enter number or 'q': ")) != "q":
    print(f"You entered: {x}")