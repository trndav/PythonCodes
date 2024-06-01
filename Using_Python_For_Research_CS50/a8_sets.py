ids = set([1,2,3,4,5,6,7,8])

print(len(ids))

ids.add(10)
print(ids)

ids.pop()
ids.pop()
print(ids)
print(len(ids))

rng = set(range(16))
print(rng)

x = set([1, 3, 5, 7, 9, 11, 13, 15])
y = rng - x
print(y)
print(type(y))

c = x | y # Union
print(c)

print(set(range(6)) & set([1,2,3,4])) # Intersection

word = "antidisestablishmentarianism"
print(word)
print(set(word))
print(len(set(word)))
print(str(set(word)))
d = set(word)
f = "" + "".join(sorted(d)) + ""
print(f)
print(d)