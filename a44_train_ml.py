# Train ML

from sklearn.model_selection import train_test_split

# Sample data
X = [[1], [2], [3], [4], [5], [6]]  # Features
y = [10, 20, 30, 40, 50, 60]        # Target values

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training features:", X_train)
print("Testing features:", X_test)
print("Training targets:", y_train)
print("Testing targets:", y_test)
