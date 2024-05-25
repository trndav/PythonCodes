# This will run, returning nothing
# class Dog:
#     def __init__(self):
#         self.bark()
# *******


# def make_class(x):
#     class Dog:
#         def __init__(self, name):
#             self.name = name 
#         def print_value(self):
#             print(x)
#     return Dog 

# cls = make_class(10)
# print(cls)
# # Returns: <class '__main__.make_class.<locals>.Dog'>


# def make_class(x):
#     class Dog:
#         def __init__(self, name):
#             self.name = name 
#         def print_value(self):
#             print(x)
#     return Dog 

# cls = make_class(10)
# d = cls("Bob")
# print(d.name)
# d.print_value()
# Returns: Bob, 10


# for i in range(5):
#     def show():
#         print(i*2)
#     show()
# # Returns 0, 2, 4, 6, 8


# for i in range(5):
#     def show():
#         print(i*2)
# show()
# # Returns 8

# import inspect

# def func(x):
#     if x == 1:
#         def rv():
#             print("X is equal to 1")
#     else:
#         def rv():
#             print("X is not 1")
#     return rv
# new = func(1)
# new()
# new2 = func(2)
# new2()

# print(id(new)) # Memory address
# print(id(func))

# print(inspect.getmembers(new))
# print("**"*20)
# print(inspect.getsource(new)) # Source of variable


import inspect
from queue import Queue

print(inspect.getsource(Queue)) # Source of variable


