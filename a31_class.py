# Class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def introduce(self):
        return f"Hi! My name is {self.name} and I am {self.age} years old."
    
x = Person("Bob", 21)

print(x.introduce())