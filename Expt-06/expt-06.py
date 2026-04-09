import numpy as np
from sklearn.decomposition import PCA

# 1. Prepare the Data (Height in cm, Weight in kg)
# These features are typically correlated.
X = np.array([
    [170, 65], [180, 80], [160, 55], 
    [185, 85], [155, 50], [175, 72]
])

# 2. Initialize and Train PCA
# We want to reduce 2 features down to 1 Principal Component
pca = PCA(n_components=1)
X_reduced = pca.fit_transform(X)

# 3. Results
print("Original Data (First 2 rows):")
print(X[:2])

print("\nReduced Data (First 2 rows):")
print(X_reduced[:2])

print(f"\nVariance captured by this 1 component: {pca.explained_variance_ratio_[0]:.2%}")