import random
import matplotlib.pyplot as plt
import numpy as np

q = random.choice(["Head", "Tail"])
print(q)

w = random.choice([0, 1])
print("Zero or one:", w)

dice = random.choice([1,2,3,4,5,6])
print("Dice:", dice)

dice2 = random.choice(range(7))
print("Dice2:", dice2)

dice3 = random.choice(range(1,7))
print("Dice3:", dice2)

# 3 dices sum
e = [random.choice(range(1,7)), random.choice(range(1,9)), random.choice(range(1,11))]
print("All 3 dices roll was:", str(e) + " and sum is:", str(sum(e)))


print(random.choice(list([1,2,3,4])))
print(sum(random.choice(range(10)) for i in range(10)))


# Dice roll histogram
# def roll():
#     rolls = []
#     for k in range(100):    
#         rolls.append(random.choice(range(1,7)))
#     return rolls
# plt.figure()
# plt.subplot(221)
# plt.hist(roll(), bins = np.linspace(1, 7, 7))
# plt.subplot(222)
# plt.hist(roll(), bins = np.linspace(1, 7, 7))
# plt.subplot(223)
# plt.hist(roll(), bins = np.linspace(1, 7, 7))
# plt.subplot(224)
# plt.hist(roll(), bins = np.linspace(1, 7, 7))
# plt.show()


# roulette probability 2 dices
# sy = []
# for rep in range(1000):
#     s = 0
#     for k in range(2):
#         a = random.choice(range(1,7))
#         s = s + a
#     sy.append(s)
# print(sy, min(sy), max(sy))
# plt.hist(sy)
# plt.show()

print("*"*20)

print(np.random.random())
print(np.random.random(5))
print(np.random.random((3,4)))
print(np.random.normal(0, 1)) # Standard normal distribution
print(np.random.normal(0, 1, 5)) # Array of 5 numbers
print(np.random.normal(0, 1, (2, 5))) # Matrix
print(np.random.randint(1,7))

X = np.random.randint(1,7, (10000, 10))
# print(np.random.randint(1,7, (10, 3)))
# print(X.shape)
# print(np.sum(X))
# print(np.sum(X, axis=0))
# print(np.sum(X, axis=1))

Y = np.sum(X, axis=1)
# print(Y)
# plt.hist(Y)
# plt.show()


print(np.random.random((2,3,4)))
print(np.random.normal(1,2,3))