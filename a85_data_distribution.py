import numpy
import matplotlib.pyplot as plt

# Create an array containing 250 random floats between 0 and 5
x = numpy.random.uniform(0.0, 5.0, 250)

print(x)

plt.hist(x, 5)
plt.show()