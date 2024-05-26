
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

    def __call__(self, y):
        print("Function call y: ", y)

    def __len__(self):
        return len(self.name)

p = Person("Bob")
p * 4
print(p) # Print memory address location
p(5)
print(len(p))

print("*"*22)


from queue import Queue as q
import inspect

# q = Queue()
# print(q)
# print(inspect.getsource(Queue))

class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"
    
    def __add__(self, item):
        self.put(item)
    
    def __sub__(self, item):
        self.get()
    
qu = Queue()
qu + 9
qu + 8
qu - 55
print(qu)
qu - None 
print(qu)