for x in range(3):
    print(x)

names = ["Bob", "Alan", "Oliver"]
for name in names:
    print(name)

for c in range(len(names)):
    print(names[c], end=", ")
print()

dic = {"Bob": 44, "Alan": 36, "Oliver": 54}
print(dic.keys)
print(dic.keys())

for name in dic.keys():
    print(name,dic[name], end=", ")
print()


for name in dic:
    print(name, dic[name], end=", ")
print()


for name in sorted(dic):
    print(name, dic[name], end=", ")
print()


for name in sorted(dic, reverse=True):
    print(name, dic[name], end=", ")
print()


bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}
for bear in bears:
    if bears[bear] == "friendly":
        print(f"Hello, {bear} bear!")
    else:
        print("odd")


n = 17
is_prime = True
for i in range(2,n):
    if n % i == 0:
        is_prime = False
print(is_prime)


n=100
number_of_times = 0
while n >= 1:
    n //= 2
    number_of_times += 1
    print(n)
print(number_of_times)