# Shopping list

print("--Shopping List Manager--")
print(" 1. Add an item\n 2. Remove an item\n 3. View shopping list\n 4. Exit\n")

cart = []

while True:
    try: 
        a = int(input("Choose: "))
        if a == 4:
            print("Exiting. Good bye!")
            break

        elif a == 1:
            b = input("What to add to cart? ")
            cart.append(b)
            print(f"{b} was added to cart.")

        elif a == 2:
            b = input("What to remove from cart? ")
            if b in cart:
                cart.remove(b)
                print(f"{b} was removed from cart.")
            else:
                print(f"{b} is not in the cart.")
        
        elif a == 3:
            if cart:
                print(f"Your cart contains: {', '.join(cart)}")
            else:
                print("Your cart is empty.")
        
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
    
    except ValueError:
        print("Invalid option. Try again.")
        continue
