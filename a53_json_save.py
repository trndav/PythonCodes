import json

def append_data():
    new_data = {
        "name": input("Enter your name: "),
        "age": int(input("Enter your age: ")),
        "email": input("Enter your email: ")
    }

    try:
        with open("a53_user_data.json", "r") as file:
            data = json.load(file)
        
        # Ensure the file contains a list
        if isinstance(data, dict):
            print("Fixing JSON file structure.")
            data = [data]  # Convert the dictionary into a list

    except FileNotFoundError:
        data = []

    data.append(new_data)

    with open("a53_user_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data added successfully!")

# Function to read all user data
def read_data():
    try:
        with open("a53_user_data.json", "r") as file:
            data = json.load(file)

        # Ensure the file contains a list
        if isinstance(data, dict):
            print("JSON file contains unexpected structure. Cannot display.")
            return

        print("\nAll User Details:")
        for entry in data:
            print(f"Name: {entry['name']}, Age: {entry['age']}, Email: {entry['email']}")

    except FileNotFoundError:
        print("No data found! Please add data first.")

# Menu
def main():
    while True:
        print("\n1. Add User Data")
        print("2. Read All User Data")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            append_data()
        elif choice == "2":
            read_data()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
