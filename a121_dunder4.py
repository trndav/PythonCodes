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

    def __contains__(self, y):
        return y in self.items

x = Backpack(["apple", "cheese", "rock", "figs"])
print(x.items)
print("figs" in x)