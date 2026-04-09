import numpy as np
from sklearn.cluster import KMeans

# 1. Prepare the Data
# Features: [Total Annual Spend ($), Number of Purchases]
X = np.array([
    [100, 2], [150, 3], [120, 2],    # Group A (Low spenders)
    [5000, 20], [5500, 25], [5200, 22], # Group B (High-value VIPs)
    [2000, 50], [2100, 45], [1900, 48]  # Group C (Frequent moderate spenders)
])

# 2. Initialize and Train the Model
# We set n_init="auto" to satisfy modern sklearn requirements
kmeans = KMeans(n_clusters=3, n_init="auto", random_state=42)
kmeans.fit(X)

# 3. Get Cluster Assignments and Centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# 4. Results
print("Customer Cluster Assignments:")
for i, customer in enumerate(X):
    print(f"Customer {i+1} {customer} -> Cluster {labels[i]}")

print("\nCluster Center Locations (Centroids):")
print(centroids)