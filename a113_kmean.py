# KMeans groups similar points together into k clusters — without knowing any labels

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate random 2D points
X = np.random.rand(100, 2)
print(X)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Get cluster assignments and centers
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Plot
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', label="Data points")
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label="Centers")
plt.title("KMeans Clustering")
plt.legend()
plt.show()
