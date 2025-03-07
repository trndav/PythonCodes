# 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
from sklearn.datasets import fetch_california_housing
data = fetch_california_housing()

# Convert to a DataFrame for better readability
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Price'] = data.target  # Add target column

# Display first few rows
print(df.head())


# Predict house prices using the average number of rooms per house (AveRooms)
# Select one feature (AveRooms) and target variable (Price)
X = df[['AveRooms']]  # Feature
y = df['Price']       # Target variable

# Convert to 2D NumPy arrays which Scikit-learn models prefer (1, 1)
X = X.to_numpy().reshape(-1, 1)
y = y.to_numpy()


# Split dataset into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)


# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Get model parameters (slope & intercept)
slope = model.coef_[0]
intercept = model.intercept_

print(f"Mean Squared Error: {mse}")
print(f"Coefficient (slope): {slope}")
print(f"Intercept: {intercept}")


# Ask user for input
num_rooms = float(input("Enter the number of rooms: "))

# Predict house price based on user input
predicted_price = model.predict(np.array([[num_rooms]]))[0]  # Convert input to 2D array

print(f"Predicted House Price: ${predicted_price * 100000:.2f}")


# Plot the regression line
plt.scatter(X_test, y_test, color='blue', label="Actual Prices")
plt.plot(X_test, y_pred, color='red', linewidth=2, label="Predicted Prices")
plt.xlabel("Average Rooms per House")
plt.ylabel("House Price")
plt.title("Linear Regression: Predicting House Prices")
plt.legend()
plt.show()
