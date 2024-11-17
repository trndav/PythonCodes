# Dictionaries

# Basic Syntax
# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "job": "Engineer"
# }

# # Access values
# print(my_dict["name"])  # Output: Alice

# # Add or update a value
# my_dict["city"] = "New York"

# # Remove a key-value pair
# del my_dict["job"]

# # Check if a key exists
# if "age" in my_dict:
#     print("Age is present.")


# Managing contact list
# contacts = {
#     "John": "john@example.com",
#     "Alice": "alice@example.com"
# }

# # Add a new contact
# contacts["Bob"] = "bob@example.com"

# # Get contact info
# print(contacts["Alice"])  # Output: alice@example.com

# # Remove a contact
# del contacts["John"]

# # List all contacts
# for name, email in contacts.items():
#     print(f"{name}: {email}")



def add_contact(phonebook):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    age = input("Enter your age: ")
    phonebook[name] = {"phone": phone, "age": age}
    print(f"Added {name} with number {phone}, age {age}.")

def search_contact(phonebook):
    name = input("Enter name to search: ")
    if name in phonebook:
        phone = phonebook[name]["phone"]
        age = phonebook[name]["age"]
        print(f"{name}'s number is {phone}, age {age}.")
    else:
        print("Contact not found.")

def delete_contact(phonebook):
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"{name} has been deleted.")
    else:
        print("Contact not found.")

def list_contacts(phonebook):
    if phonebook:
        for name, details in phonebook.items():
            phone = details["phone"]
            age = details["age"]
            print(f"{name}: {phone}, age: {age}")
    else:
        print("Phonebook is empty.")

def main():
    phonebook = {}
    while True:
        print("\n1. Add contact\n2. Search contact\n3. Delete contact\n4. List all contacts\n5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_contact(phonebook)
        elif choice == "3":
            delete_contact(phonebook)
        elif choice == "4":
            list_contacts(phonebook)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
