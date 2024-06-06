ml = [4,7,2,8,45,78,21,11]
ml.sort()
print(ml, min(ml), max(ml))

ml.remove(45)
print(ml)

class MyList(list): # list - inheritance
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))

x = MyList(ml)
print(dir(x))
print(x)
x.remove_min()
print(x)
x.remove_max()
print(x)


class NewList(list):
    def remove_max(self):
        self.remove(max(self))
    def append_sum(self):
        self.append(sum(self))

x = NewList([1,2,3])
while max(x) < 10:
    x.remove_max()
    x.append_sum()

print(x)