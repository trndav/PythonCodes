# Named tuple

from collections import namedtuple

# Define a named tuple called 'Car'
Car = namedtuple('Car', ['brand', 'model', 'year'])
Names = namedtuple('Bob', ['age', 'personality', 'city'])

# Create instances of Car
car1 = Car(brand="Toyota", model="Corolla", year=2020)
car2 = Car(brand="Honda", model="Civic", year=2019)
name1 = Names(age="29", personality="pessimist", city="New York")

# Access fields like an object
print(car1.brand)  
print(car2.year)   

# Named tuples are still tuples, so indexing works too
print(car1[1]) 

print(name1.personality)
print(name1.city)
print(name1[0])
print(Names.__name__)