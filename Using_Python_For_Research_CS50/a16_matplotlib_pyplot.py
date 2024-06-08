import matplotlib.pyplot as plt
import numpy as np

# x = [0, 1, 4, 7, 8, 9, 6, 2, -10, 4, 22]
# plt.plot(x)
# plt.show()

# y = np.linspace(0, 10, 20)
# c = y**2.0
# c2 = y**1.5
# print(y)
# print(c)
# print(c2)

# # plt.plot(y,c)
# # plt.show()


# plt.plot(y, c, "rd-", linewidth=2, markersize=6, label="Quantity") # bo- blue, circles, rd-
# plt.plot(y, c2, "bo-", linewidth=2, markersize=6, label="Quality") # label goes with plt.legend
# plt.xlabel("Years")
# plt.ylabel("Profits")
# plt.axis([-0.5, 10.5, -5, 105]) # [xmin, xmax, ymin, ymax]
# plt.legend(loc = "center") # Legend info (from label)
# plt.savefig("myplot.jpeg") # Save plot
# # plt.show()


# y = np.logspace(-1, 1, 40) # linspace, logspace
# c = y**2.0
# c2 = y**1.5
# print(y)
# print(c)
# print(c2)

# plt.loglog(y, c, "rd-", linewidth=2, markersize=6, label="Quantity") # bo- blue, circles, rd-
# plt.loglog(y, c2, "bo-", linewidth=2, markersize=6, label="Quality") # label goes with plt.legend
# plt.xlabel("Years")
# plt.ylabel("Profits")
# plt.axis([-0.5, 10.5, -5, 105]) # [xmin, xmax, ymin, ymax]
# plt.legend(loc = "upper left") # Legend info (from label)
# plt.savefig("myplot.jpeg") # Save plot
# #plt.show()


# print("linspace: ",np.linspace(1, 3, 10))


# x = np.logspace(0,1,10)
# y = x**2
# plt.loglog(x,y,"bo-")
# plt.show()

# plt.figure()
# x = np.random.normal(size=1000)
# plt.subplot(x)
# plt.hist(x)
# plt.hist(x, bins=np.linspace(-5, 5, 21))
# # # plt.show()
# q = np.random.gamma(2, 3, 100)
# plt.subplot(q)
# plt.hist(q, bins = 30, cumulative=True, histtype = "step")

x = np.random.normal(size=1000)
plt.figure()
plt.subplot(121)
plt.hist(x, bins = 30)
plt.subplot(122)
plt.hist(x, bins = 30, cumulative = True)
# plt.subplot(223)
# plt.hist(x, bins = 30, histtype = "step")
# plt.subplot(224)
# plt.hist(x, bins = 30, cumulative = True, histtype = "step")
plt.show()


