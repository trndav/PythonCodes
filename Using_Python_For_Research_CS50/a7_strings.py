S = "Python"
print(len(S))
print(S[0:2])

print(S[-4])
print(S[-4:])

print("y" in S)
print("Py" in S)
print("b" in S)

print(S[0:2]*10)

x = 8
print(S + "", str(x))

print(S)
print(S.replace("Python", "Python rocks"))
print(S)
y = S.replace("Python", "Python is the best")
print(y)

print(type(y))
print(len(y))

a = y.split(" ")
print(a)
print(type(a))
print(len(a))
print(a[1:])
print(type(a[0]))

print(a[0].upper())

import string 
print(string.digits)

print(str(range(10)))

v = "125,000"
print(v.isdigit())