# Second largest

x = input("Type few numbers:\n").split(" ")
a = []
for i in x:
    a.append(i)
a.sort(reverse=True)
print(a[1])
