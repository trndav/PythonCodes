class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is a dog named {self.name}"

dog = Dog("Bobby")
print(dog)

class Backpack:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        return Backpack(self.items + other.items)
    
    def __str__(self):
        return f"Backpack contains: {', '.join(self.items)}"

bag1 = Backpack(["book", "pen"])
bag2 = Backpack(["laptop"])
big_bag = bag1 + bag2

print(len(big_bag))  # 3
print(big_bag)
