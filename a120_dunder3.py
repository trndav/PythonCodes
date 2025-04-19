class Backpack:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        return Backpack(self.items + other.items)

    def __str__(self):
        return f"Backpack contains: {', '.join(self.items)}"

    def __getitem__(self, index):
        return self.items[index]

x = Backpack(["belt", "gun", "socks"])
print(x[1])
print(x)