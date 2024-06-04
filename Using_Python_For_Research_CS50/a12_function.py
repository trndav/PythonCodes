def add(a, b):
    return a + b 
print(add(5, 6))

def add_sub(a, b):
    mysum = a + b 
    mydiff = a - b 
    return (mysum, mydiff)
print(add_sub(3, 8))

new = add_sub
print(new(8, 9))

def modifylst(lst):
    lst[0] *= 6
lst1 = [1,2,3]
modifylst(lst1)
print(lst1)

def modifylst(lst):
    lst[0] *= 5
    return lst
lst1 = [1,2,3]
print(modifylst(lst1))

print("**"*20)


def intersect(s1, s2):
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res 
print(intersect([1,2,3,4,5], [3,4,6,7,8]))


import random
print(random.choice([1,2,3,4,5,6]))
print(random.choice("abcdefgh"))

def password(length):
    pw = str()
    characters = "abcdefghijklmnoprstuvzyxwq0123456789.!"
    for i in range(length):
        pw = pw + random.choice(characters)
    return pw 
print(password(8))


def is_vowel(letter):
    if letter in ("aeiouy"):
        return(True)
    else:
        return(False)
print(is_vowel("b"))


def factorial(n):
    if n == 0:
        return 1
    N = 1
    for i in range(1, n+1):
        N *= i
    return(N)
print(factorial(5))