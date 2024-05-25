
# x = [1, 2, 3]
# y = [4, 5]
# c = x + y
# print(c)
# print(type(c))


class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Person name is: {self.name}"
    
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Must be int")
        self.name = (self.name + " ") * x

p = Person("Bob")
p * 4
print(p) # Print memory address location