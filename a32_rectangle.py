# Rectangle

class Rectangle:
    def __init__(self, height, width):
        self.height = height 
        self.width = width

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return (self.width + self.height) * 2
    
    def check(self):
        if self.width == self.height:
            return f"With height: {self.height}, and width: {self.width}, object is a square."
        else:
            return f"With height: {self.height}, and width: {self.width}, object is a rectangle."
    
x = Rectangle(2, 3)
print(x.area())
print(x.perimeter())
print(x.check())