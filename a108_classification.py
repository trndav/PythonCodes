import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

# Load the dataset
data = load_breast_cancer()

# Convert to Pandas DataFrame for easy viewing
df = pd.DataFrame(data.data, columns=data.feature_names)

# Add the target column
df['Target'] = data.target

# Show the first 5 rows
print(df.head())


# Train model
from sklearn.model_selection import train_test_split

# Separate features and target
X = df.drop(columns=['Target'])  # Features
y = df['Target']  # Target (Malignant or Benign)

# Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training data size: {X_train.shape}")
print(f"Testing data size: {X_test.shape}")


# Logistic Regression for classification
from sklearn.linear_model import LogisticRegression

# Create and train the model
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)


# Test model
from sklearn.metrics import accuracy_score

# Make predictions on test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
