import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Wine Dataset
data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)
print(df)
df['Target'] = data.target  # Class labels (0, 1, 2)

# Split into Training & Testing Data
X = df.drop(columns=['Target'])
y = df['Target']
print("y:", y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("X_train before scaler: ", X_train)

# Standardize Features (Feature Scaling)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
print("X_train: ", X_train)
X_test = scaler.transform(X_test)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

# Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")


from sklearn.model_selection import cross_val_score

# Perform cross-validation with 5 folds
cv_scores = cross_val_score(model, X_train, y_train, cv=5)
print(f"Cross-validation accuracy: {np.mean(cv_scores) * 100:.2f}%")