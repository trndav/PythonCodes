import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# Load the digits dataset
digits = load_digits()

# Get user input
num = int(input("Enter a digit (0-9) to visualize: "))

# Find the first occurrence of the number in the dataset
# returns an array of indices where digits.target matches the user input
index = np.where(digits.target == num)[0][0]

# Get the image
image = digits.images[index]

# Display the image
plt.imshow(image, cmap='gray')
plt.title(f"Handwritten Digit: {num}")
plt.axis("off")
plt.show()

x = digits.target # == num
print(x)