#vacuum agent

def simple_reflex_vacuum_agent(location, status):
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Left'

# Simulation
current_location = 'A'
current_status = 'Dirty'

action = simple_reflex_vacuum_agent(current_location, current_status)
print(f"Agent in {current_location} sees {current_status} -> Action: {action}")

#smart light agent

class SmartLightAgent:
    def __init__(self, threshold=30):
        self.threshold = threshold

    def act(self, light_level):
        """Simple reflex logic: Condition -> Action"""
        if light_level < self.threshold:
            return "ON"
        else:
            return "OFF"

# --- Simulation ---
agent = SmartLightAgent(threshold=30)

# Simulated sensor readings (Environment)
# 10 is dark (night), 80 is bright (daylight), 25 is dusk
sensor_readings = [10, 25, 80, 45, 15]

print(f"{'Sensor Value':<15} | {'Agent Action':<12}")
print("-" * 30)

for level in sensor_readings:
    action = agent.act(level)
    print(f"{level:<15} | {action:<12}")