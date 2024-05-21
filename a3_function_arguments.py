def complicated_function(x, y):
    print(x, y)
complicated_function(y = 1, x = 3) # Or (y = 3, x = 5)


def complicated_function(x, y, z):
    print(x, y)
complicated_function(1, z = 6, y = 3)


def complicated_function(x, y, z = None): # z is optional
    print(x, y, z)
complicated_function(y = 1, x = 3) 


def complicated_function(x, y, *args): 
    print(x, y, args)
    pass
complicated_function(1, 3, 8, 9, 10) 


def complicated_function(*args): 
    return args
for i in complicated_function(1, 2, 4, 6, 8):
    print(i, end=", ")
print()
print("*"*20)


def complicated_function2(*args, **kwargs): 
    print(args, kwargs)
complicated_function2(55, 77, x = 1, s = "hi", b = True) 


def complicated_function2(a, b, c = True, d = False): 
    print(a, b, c, d)
complicated_function2(1, 5) 