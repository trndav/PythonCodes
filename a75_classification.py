import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
wine = load_wine()
X, y = wine.data, wine.target  # Features & Labels

# Print dataset info
print("Feature names:", wine.feature_names)
print("Target classes:", wine.target_names)

import pandas as pd

# Convert to DataFrame for easier exploration
df = pd.DataFrame(X, columns=wine.feature_names)
df['target'] = y

# Show first 5 rows
print(df.head())

# Plot feature distributions
sns.pairplot(df, hue="target", diag_kind="kde")
plt.show()

# Split into 80% training and 20% testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create Random Forest classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf.fit(X_train, y_train)

# Predict on test data
y_pred = rf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Detailed classification report
print(classification_report(y_test, y_pred, target_names=wine.target_names))

# Get feature importances
importances = rf.feature_importances_

# Sort feature importances
indices = np.argsort(importances)[::-1]

# Plot feature importance
plt.figure(figsize=(10, 5))
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), np.array(wine.feature_names)[indices], rotation=90)
plt.xlabel("Feature Importance")
plt.ylabel("Score")
plt.title("Feature Importance in Random Forest")
plt.show()
