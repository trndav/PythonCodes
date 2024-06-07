import matplotlib.pyplot as plt
import numpy as np

# x = [0, 1, 4, 7, 8, 9, 6, 2, -10, 4, 22]
# plt.plot(x)
# plt.show()

y = np.linspace(0, 10, 20)
c = y**2.0
c2 = y**1.5
print(y)
print(c)
print(c2)

# plt.plot(y,c)
# plt.show()


plt.plot(y, c, "rd-", linewidth=4, markersize=12) # bo- blue, circles, rd-
plt.show()
