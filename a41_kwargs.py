# Kwargs

def book_details(name, **kwargs):
    details = f"Book title: {name}\n"
    if kwargs:
        details += "Additional details:\n"
        for key, value in kwargs.items():
            details += f"  {key.capitalize()}: {value}\n"
    else:
        details += "No additional keywords provided."
    return details
print(book_details("Bible", genre="Religion", author="Christians"))