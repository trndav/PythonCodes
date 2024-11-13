# Shopping list with functions (a10)
# To do: Add functionality to save the cart to a file and load it when the program starts.

def welcome():
    print("--Shopping List Manager--\n 1. Add an item\n 2. Remove an item\n 3. View shopping list\n 4. Exit\n")

def exit_cart():
    print("Exiting. Good bye!")

def add_to_cart(cart):
    b = input("What to add to cart? ")
    if b in cart:
        print(f"{b} is already in cart.")
    else:
        cart.append(b)
        print(f"{b} was added to cart.")

def remove_from_cart(cart):
    b = input("What to remove from cart? ")
    if b in cart:
        cart.remove(b)
        print(f"{b} was removed from cart.")
    else:
        print(f"{b} is not in the cart.")

def cart_list(cart):
    if cart:
        print(f"Your cart contains: {', '.join(cart)}")
    else:
        print("Your cart is empty.")

welcome()
def main():
    cart = []    
    while True:    
           
        try: 
            a = int(input("Choose: "))
            if a == 4:
                exit_cart()
                break

            elif a == 1:
                add_to_cart(cart)
            
            elif a == 2:
                remove_from_cart(cart)

            elif a == 3:
                cart_list(cart)

            else:
                print("Invalid input. Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid option. Try again.")
            continue
main()