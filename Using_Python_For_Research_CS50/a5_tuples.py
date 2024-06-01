
T = (1, 3, 5, 7)
print(len(T))

T = T + (9, 11)
print(T)

print(T[1], T[-1])

x = 12.23
y = 23.34

coords = (x,y) # Packing
print(coords)
print(type(coords))

(x1, x2) = coords # Unpack
print(x1, "and x2 is:", x2)

loop = [(0,0), (1,1), (2,2), (3,3), (4,4), (5,5)]
for x,y in loop: # Unpack
    print("x is:", x, "y is:", y)
    print(x,y)

c = (2,3)
print(type(c))

d = (2)
print(type(d))

e = (2,)
print(type(e))

f = (2, 4, 6, 2, 3, 1, 2 , 8)
print(f.count(2))
print(sum(f))