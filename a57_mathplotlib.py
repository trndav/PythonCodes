# Matplotlib

import matplotlib.pyplot as plt

x = [1, 12, 3, 14, 5]
y = [2, 4, 6, 8, 10]
c = [12, 14, 16, 18, 20]
d = [3, 11, 27, 18, 29]

#plt.plot(x, y, c, d)

plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Simple Line Graph')

plt.plot(x, y, color='red', linestyle='--', marker='o', label='Dashed Line')
plt.plot(x, c, color='blue', linestyle='-', marker='s', label='Solid Line')
plt.scatter(x, d, color='purple', label='Data Points')
plt.bar(x, y, color='orange', label='Bar Chart')

plt.grid(True)
plt.legend()
plt.savefig('a57_matplotlib.png')
plt.show()
