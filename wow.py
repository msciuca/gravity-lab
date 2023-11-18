import math

def calculate_gravity(distance, time):
    gravity = 2 * distance / math.pow(time, 2)  # Using math.pow instead of **2**
    return gravity  # Returning the calculated gravity value

distance = float(input("Enter distance (meters): "))
time = float(input("Enter time (seconds): "))

gravity = calculate_gravity(distance, time)
print("The acceleration due to gravity is:", gravity, "m/s²")

