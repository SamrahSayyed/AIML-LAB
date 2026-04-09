import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Define the Universe (Temperature range from 0 to 40 degrees)
temp = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')

# 2. Define Fuzzy Membership Functions
# 'trimf' creates a triangle shape: [start, peak, end]
temp['cold'] = fuzz.trimf(temp.universe, [0, 0, 20])
temp['comfy'] = fuzz.trimf(temp.universe, [15, 22, 30])
temp['hot'] = fuzz.trimf(temp.universe, [25, 40, 40])

# 3. Simulate a specific temperature
current_temp = 24

# 4. Calculate Membership Degrees
val_cold = fuzz.interp_membership(temp.universe, temp['cold'].mf, current_temp)
val_comfy = fuzz.interp_membership(temp.universe, temp['comfy'].mf, current_temp)
val_hot = fuzz.interp_membership(temp.universe, temp['hot'].mf, current_temp)

# 5. Results
print(f"At {current_temp}°C, the room is:")
print(f"- Cold: {val_cold:.2f}")
print(f"- Comfortable: {val_comfy:.2f}")
print(f"- Hot: {val_hot:.2f}")