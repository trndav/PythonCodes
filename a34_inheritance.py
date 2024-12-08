# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."

# Subclass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof Woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

# Test the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy")

print(animal.speak())  # Output: Generic Animal makes a sound.
print(dog.speak())     # Output: Buddy says: Woof Woof!

animal = Animal("Cat")
cat = Cat("Lisa")

print(animal.speak()) 
print(cat.speak())   