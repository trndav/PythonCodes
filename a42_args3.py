# Args part 3

def lots_of_args(name, *args):
    print(f"{name} is the best dog in the world.")
    print(f"He is {', '.join(x for x in args)}.")

lots_of_args("Bob", "good", "kind", "funny", "brave")

print("*"*20)

def lots_of_kwargs(name, **kwargs):
    print(f"{name} is cat.")
    if kwargs:
        for key, value in kwargs.items():
            print(f" {key.capitalize()}: {value}")

    
lots_of_kwargs("Lily", age=4, color="white")