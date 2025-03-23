import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load digits dataset
digits = load_digits()

# Features (image pixel values) and target (actual digit)
X = digits.data
y = digits.target

# Display one sample image
plt.gray()
plt.matshow(digits.images[0])
plt.show()
print(f"Label: {digits.target[0]}")
print(f"Data: {digits.data[:5]}")
print(f"Test: {digits.target[:5]}")
print(f"Shape: {digits.data.shape}")

# Split dataset into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features for better performance
# Some features may have larger values (e.g., pixel intensities from 0-255), while others are smaller. 
# Scaling prevents the model from favoring larger values.
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Use a Random Forest model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict on test data
y_pred = clf.predict(X_test)

# Compute accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
