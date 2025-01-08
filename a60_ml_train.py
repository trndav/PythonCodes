# Machine learning train

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# X represents the size of the house (in square meters)
# y represents the price of the house (in $1000)
X = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140]).reshape(-1, 1)
y = np.array([200, 240, 280, 320, 360, 400, 440, 480, 520, 560])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict prices
predicted_prices = model.predict(X_test)

plt.scatter(X, y, color='blue', label='Actual Prices')
plt.plot(X, model.predict(X), color='red', label='Prediction Line')
plt.scatter(X_test, predicted_prices, color='green', label='Predicted Prices (Test)')
plt.xlabel('House Size (sq meters)')
plt.ylabel('House Price ($1000)')
plt.legend()
plt.show()

# Print test predictions
for i, size in enumerate(X_test):
    print(f"Predicted price for house size {size[0]} sq meters: ${predicted_prices[i]:.2f}K")
print(X_test)