#

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_breast_cancer

# Load the dataset
data = load_breast_cancer()

# Convert to Pandas DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = data.target  # 0 = Malignant, 1 = Benign

print(df.columns) # Print dataframe columns
print(df.head()) # Display first few rows


# Features (X) and target variable (y)
X = df.drop(columns=['Target']).to_numpy()  # Convert to NumPy array
y = df['Target'].to_numpy()  # 0 = Malignant, 1 = Benign


# Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Use Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print classification report
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred, target_names=["Malignant", "Benign"]))


# Ask user for input (example with 3 features, but dataset has 30 features)
print("\nEnter tumor measurements:")
radius = float(input("Enter mean radius: "))
texture = float(input("Enter mean texture: "))
perimeter = float(input("Enter mean perimeter: "))

# Convert input to NumPy array & normalize
user_input = np.array([[radius, texture, perimeter] + [0] * 27])  # Fill with zeros for simplicity
user_input = scaler.transform(user_input)

# Predict tumor type
predicted_class = model.predict(user_input)[0]
prediction = "Benign" if predicted_class == 1 else "Malignant"

print(f"Predicted Tumor Type: {prediction}")
