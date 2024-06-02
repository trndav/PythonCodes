age = {} # empty dict

age = dict() # dict

age = {"Bob": 19, "Ana": 23, "Tim": 32}

print(age["Bob"])

age["Bob"] = 22
print(age["Bob"])

for key in age:
    print(key)

names = age.keys()
print(type(names))

age["Rock"] = 30
print(age)
print(names)

values = age.values()
print(values)

print("Bob" in age)

print(id(names))
print(id(values))

L = [1,2,3]
M = L 
print(M is L)
M = list(L)
print(M is L)

G = L[:]
print(G == L)
print(G is L)