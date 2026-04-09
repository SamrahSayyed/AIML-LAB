import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text

# 1. Prepare the Data
# Features: [Credit Score, Annual Income in $1000s]
X = np.array([
    [750, 80], [700, 45], [600, 90], [550, 30], [800, 100], [620, 25]
])

# Labels: 1 for Approved, 0 for Denied
y = np.array([1, 1, 1, 0, 1, 0])

# 2. Initialize and Train the Model
# We set max_depth to keep the tree simple
clf = DecisionTreeClassifier(max_depth=2)
clf.fit(X, y)

# 3. Classify a New Applicant
# Applicant: 610 Credit Score, $40k Income
new_applicant = [[610, 40]]
prediction = clf.predict(new_applicant)

# 4. Results
status = "Approved" if prediction[0] == 1 else "Denied"
print(f"Loan Status for Applicant (610, $40k): {status}")

# View the logic of the tree
tree_rules = export_text(clf, feature_names=['Credit Score', 'Income'])
print("\nDecision Tree Logic:")
print(tree_rules)