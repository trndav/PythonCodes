# Saving dict, JSON

import json

def save_phonebook(phonebook):
    with open("a14_phonebook.json", "w") as file:
        json.dump(phonebook, file)
    print("Phonebook saved.")

def load_phonebook():
    try:
        with open("a14_phonebook.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No existing phonebook found. Starting fresh.")
        return {}

def add_contact(phonebook):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    age = input("Enter age: ")
    phonebook[name] = {"phone": phone, "age": age}
    print(f"{name}, age: {age}, added to phonebook with phone: {phone}.")
    save_phonebook(phonebook)

def list_contacts(phonebook):
    if phonebook:
        for name, details in phonebook.items():
            print(f"{name}, phone: {details['phone']}, age: {details['age']}.")
    else:
        print("Phonebook is empty.")

def main():
    phonebook = load_phonebook()
    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. List Contacts")
        print("4. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_contact(phonebook)
            elif choice == 2:
                delete_contact(phonebook)
            elif choice == 3:
                list_contacts(phonebook)
            elif choice == 4:
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

main()