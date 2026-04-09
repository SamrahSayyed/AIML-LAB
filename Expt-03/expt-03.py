import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Prepare the Data
# House Size (Square Feet) - Independent Variable (X)
X = np.array([[1500], [1800], [2400], [3000], [3500]]) 
# House Price (USD) - Dependent Variable (y)
y = np.array([250000, 300000, 400000, 500000, 580000])

# 2. Initialize and Train the Model
model = LinearRegression()
model.fit(X, y)

# 3. Make a Prediction
house_size = [[2800]]
predicted_price = model.predict(house_size)

# 4. Model Coefficients
slope = model.coef_[0]
intercept = model.intercept_

print(f"Prediction for a 2,800 sq ft house: ${predicted_price[0]:,.2f}")
print(f"Model Equation: Price = {slope:.2f} * (Size) + {intercept:.2f}")