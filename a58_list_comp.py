
x = 1
y = []
for x in range(1, 10):
    x = x * x
    print(x)
    y.append(x)
print(y)

a = []
for i in y:
    if i % 2 == 0:
        a.append(i)
print(f"a is: {a}")

b = ["alpha", "beta"]
c = [item.upper() for item in b]
print(c)

d = [1, 2, 3]
e = [4, 5, 6]
f = [(k, l) for k in d for l in e]
print(f)
