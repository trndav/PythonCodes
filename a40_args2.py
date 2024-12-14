# Order detail

def order_details(name, *args, **kwargs):
    print(f"Customer: {name}")

    if args:
        print(f"Items ordered: {', '.join(args)}")
    else:
        print(f"No items ordered.")

    if kwargs:
        print(f"Delivery details:")
        for key, value in kwargs.items():
            print(f" {key.capitalize()}: {value}")
    else:
        print(f"No delivery details.")

order_details("Bob", "Pizza", "Cake", address="Zg 1001", phone=223443)