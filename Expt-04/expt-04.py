import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 1. Prepare the Data
# Features: [Weight in grams, Texture Score]
X = np.array([
    [150, 4], [170, 3], [160, 5],  # Oranges (Label 0)
    [250, 7], [300, 8], [280, 9]   # Grapefruits (Label 1)
])

# Labels: 0 for Orange, 1 for Grapefruit
y = np.array([0, 0, 0, 1, 1, 1])

# 2. Initialize and Train the Model (k=3)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# 3. Classify a New Fruit
# New fruit: 220g with a texture score of 6
new_fruit = [[220, 6]]
prediction = knn.predict(new_fruit)
probabilities = knn.predict_proba(new_fruit)

# 4. Results
fruit_type = "Grapefruit" if prediction[0] == 1 else "Orange"
print(f"Prediction for fruit (220g, Score 6): {fruit_type}")
print(f"Probability (Orange vs Grapefruit): {probabilities[0]}")