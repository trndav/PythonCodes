import numpy as np
import matplotlib.pyplot as plt
import time

X_0 = np.array([[0], [0]]) # Starting point of array
q = np.random.normal(0,1, (2,1000))
W = np.concatenate((X_0, np.cumsum(q, axis = 1)), axis = 1)
   
# W = np.cumsum(q, axis = 1)
# print(q)
# print("Cumsum:",W)

plt.plot(W[0], W[1], "ro-", label="Path")
plt.legend()


plt.savefig("random_walk.jpg")
plt.show()


