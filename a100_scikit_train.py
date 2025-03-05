
# 

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate sample data
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # 100 samples, 1 feature
y = 2.5 * X + np.random.randn(100, 1) * 2  # y = 2.5x + noise

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Compute Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Print model coefficients
print(f"Coefficient (slope): {model.coef_[0][0]}")
print(f"Intercept: {model.intercept_[0]}")


### 
import matplotlib.pyplot as plt

# Plot the data points
plt.scatter(X_train, y_train, color='blue', label='Training Data')
plt.scatter(X_test, y_test, color='red', label='Test Data')

# Plot the model's prediction (a straight line for linear regression)
plt.plot(X_test, y_pred, color='green', linewidth=2, label='Model Prediction')

# Labels and legend
plt.xlabel("X (Feature)")
plt.ylabel("y (Target)")
plt.title("Linear Regression Model")
plt.legend()
plt.show()
