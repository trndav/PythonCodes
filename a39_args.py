# Dynamic greet

def dynamic_greet(*args, **kwargs):
    greeting = kwargs.get("greeting")
    punctuation = kwargs.get("punctuation")

    if not args:
        print("No one to greet.")
    else:
        for name in args:
            print(f"{greeting} {name}{punctuation}")


dynamic_greet("Alice", "Bob", "Charlie", greeting="Hi", punctuation="!!")