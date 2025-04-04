from sklearn.linear_model import LogisticRegression
import numpy as np

# Training data: [hours studied]
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)

# Target: 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Train the classifier
model = LogisticRegression()
model.fit(X, y)

# Ask user for input
hours = int(input("Enter number of hours studied: "))
prediction = model.predict(np.array([[hours]]))[0]

# Output result
if prediction == 1:
    print("🎉 The student is likely to PASS!")
else:
    print("❌ The student is likely to FAIL.")
