# Class count

class Counter:
    object_count = 0

    def __init__(self, name):
        self.name = name
        Counter.object_count += 1

    @classmethod
    def get_count(x):
        return f"Number of objects created: {x.object_count}"


# Create objects
obj1 = Counter("Bob")
obj2 = Counter("Sir")
obj3 = Counter("Alan")

# Check the count using the class method
print(Counter.get_count())
obj4 = Counter("Grunf")
print(Counter.get_count())