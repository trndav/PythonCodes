#Metaclass defines rules for class

# def hi():
#     class Hi:
#         pass 
#     return Hi # We can do this bc class is also object, available to run at runtime

# Hi()


# class Test:
#     pass
# def func():
#     pass    
# print(Test)
# print(Test())
# print(type(Test()))
# print(type(func))


# class Test:
#     pass 
# print(type(Test)) # Type constructor metaclass

# Test2 = type('Test2', (), {}) # Same as class Test. (Name, bases/inheritance, attributes)
# print(type(Test2))
# print(Test2())
# print(Test2)


# Test3 = type('Test3', (), {"x":5})
# t = Test3()
# print(t, " of type: ", type(t))
# print(t.x)

# t.something = "Hi there!"
# print(t.something)


# class Foo:
#     def show(self):
#         print("Hola!")

# def add_attribute(self):
#     self.z = "Added attribute"

# Test3 = type('Test3', (Foo,), {"x":5, "add_attribute": add_attribute})
# t = Test3()
# print(t, " of type: ", type(t))
# print(t.x)
# t.show()
# t.add_attribute()
# print(t.z)


# class Meta(type):
#     def __new__(self, class_name, bases, attrs):
#         print(attrs)
#         return type(class_name, bases, attrs)

# class Dog(metaclass=Meta):
#     x = 5
#     y = 8
#     def hi(self):
#         print("hiho")


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a = {}
        for name, value in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value
        print(a)
        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x = 5
    y = 8
    def hip(self):
        print("hiho")

d = Dog()
# print(d.x)
print(d.X)
# print(d.hip())
print(d.HIP())