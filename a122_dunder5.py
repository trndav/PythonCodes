class Backpack:
    def __init__(self, items):
        self.items = items

    def __eq__(self, other):
        if not isinstance(other, Backpack):
            return False
        return self.items == other.items

bag1 = Backpack(["map", "water"])
bag2 = Backpack(["map", "water"])
bag3 = Backpack(["map", "rope"])

print(bag1 == bag2)  # True
print(bag1 == bag3)  # False

# Without __eq__:
# If you didn’t define it, bag1 == bag2 would return False 
# even if contents are the same, because the default behavior is to check 
# if they are the same object in memory, not the same contents.


