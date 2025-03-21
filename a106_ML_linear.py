import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Create training data (house size in square meters & price in $1000)
X = np.array([30, 40, 50, 60, 70, 80]).reshape(-1, 1)  # House sizes
y = np.array([100, 150, 200, 250, 300, 350])  # Prices
print(f"X is: {X}")
print(f"y is: {y}")

# Step 2: Create and train the model
model = LinearRegression()
model.fit(X, y)  # Train the model on data

# Step 3: Make a prediction (for a 55m² house)
predicted_price = model.predict([[55]])
print(f"Predicted price for 55m² house: ${predicted_price[0]*1000:.2f}")

# Step 4: Visualize the results
plt.scatter(X, y, color="blue", label="Training Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.scatter([[55]], predicted_price, color="green", marker="x", s=100, label="Predicted Price")
plt.xlabel("House Size (m²)")
plt.ylabel("Price ($1000)")
plt.legend()
plt.show()
