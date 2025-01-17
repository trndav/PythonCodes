# K-Nearest Neighbors (KNN) Classifier

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Generate Data
np.random.seed(0)
class_A = np.random.randn(20, 2) + np.array([2, 2])  # Class A around (2,2)
class_B = np.random.randn(20, 2) + np.array([-2, -2])  # Class B around (-2,-2)

# Combine the data and labels
data = np.vstack((class_A, class_B))
labels = np.array(['A'] * len(class_A) + ['B'] * len(class_B))

# Step 2: Visualize the Data
plt.scatter(class_A[:, 0], class_A[:, 1], label='Class A', color='blue')
plt.scatter(class_B[:, 0], class_B[:, 1], label='Class B', color='red')
plt.legend()
plt.title("Data Distribution")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Step 3: Implement KNN
def knn_predict(data, labels, query_point, k=3):
    # Calculate distances from the query point to all points in the dataset
    distances = [np.linalg.norm(query_point - point) for point in data]
    # Find the indices of the k nearest neighbors
    k_indices = np.argsort(distances)[:k]
    # Get the labels of the k nearest neighbors
    k_labels = [labels[i] for i in k_indices]
    # Determine the most common label (majority vote)
    most_common = Counter(k_labels).most_common(1)
    return most_common[0][0]  # Return the label with the highest count

# Step 4: Test the Classifier
query_points = np.array([[0, 0], [3, 3], [-3, -3]])
for query_point in query_points:
    predicted_class = knn_predict(data, labels, query_point, k=3)
    print(f"Query point {query_point} is predicted to be in Class {predicted_class}")

    # Plot query points and their predicted class
    plt.scatter(class_A[:, 0], class_A[:, 1], label='Class A', color='blue')
    plt.scatter(class_B[:, 0], class_B[:, 1], label='Class B', color='red')
    plt.scatter(query_point[0], query_point[1], label=f'Query {predicted_class}', color='green', marker='x')
    plt.legend()
    plt.title("KNN Prediction")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()
