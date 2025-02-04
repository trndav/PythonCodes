import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Generate random customer data (Income, Spending Score)
np.random.seed(42)
income = np.random.randint(20000, 100000, 100)  # Annual income
print(income)
spending = np.random.randint(1, 100, 100)  # Spending score
print(spending)

X = np.column_stack((income, spending))  # Combine into dataset
print(X)

# 2. Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # 3 clusters
clusters = kmeans.fit_predict(X)
print(clusters)

# 3. Visualize the clusters
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200)  # Centers
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('Customer Clusters')
plt.show()