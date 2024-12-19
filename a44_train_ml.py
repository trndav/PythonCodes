# Train ML

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample data
X = [[1], [2], [3], [4], [5]]  # Features
y = [2, 4, 6, 8, 10] # Target values

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Create the Linear Regression model
model = LinearRegression()

# Step 3: Train the model on the training data
model.fit(X_train, y_train)

# Step 4: Make predictions on the testing data
y_pred = model.predict(X_test)

# Step 5: Evaluate the model using Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

print("Training data:", X_train, y_train)
print("Testing data:", X_test, y_test)
print("Predicted values:", y_pred)
print("Mean Squared Error:", mse)
