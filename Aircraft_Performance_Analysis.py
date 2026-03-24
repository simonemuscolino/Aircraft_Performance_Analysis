import numpy as np

"""
Aircraft Performance Analysis Tool

This script computes key aircraft performance parameters including
range, endurance, aerodynamic forces, and flight dynamics.

Author: Simone Muscolino
"""

def calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed):
    endurance = fuel_capacity / fuel_consumption_rate
    return endurance * true_air_speed

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    return fuel_capacity / fuel_consumption_rate

def calculate_total_weight(payload, fuel_weight):
    return payload + fuel_weight

def calculate_cg_position(moment_list, total_weight):
    return sum(moment_list) / total_weight

def calculate_lift(cl, rho, v, s):
    return 0.5 * cl * rho * v**2 * s

def calculate_drag(cd, rho, v, s):
    return 0.5 * cd * rho * v**2 * s

def calculate_weight(mass, g):
    return mass * g

def calculate_acceleration(thrust, drag, mass):
    return (thrust - drag) / mass

def calculate_velocity(v0, acceleration, time):
    return v0 + acceleration * time

def calculate_distance(velocity, time):
    return velocity * time

def calculate_ld_ratio(lift, drag):
    return lift / drag if drag != 0 else 0

def pretty_print(data):
    print("\n=== Aircraft Performance Analysis ===\n")
    for key, value in data.items():
        print(f"{key}: {value}")
    print("\n====================================\n")

def save_to_file(data, filename="aircraft_performance_analysis.txt"):
    with open(filename, 'w') as f:
        f.write("Aircraft Performance Analysis\n\n")
        for key, value in data.items():
            f.write(f"{key}: {value}\n")

def main():
    # Input data (modificabili)
    fuel_capacity = 1000
    fuel_consumption_rate = 50
    true_air_speed = 150
    payload = 5000
    fuel_weight = 6000
    moment_list = [10000, 2500]
    total_weight_input = 1500

    cl = 1.5
    rho = 1.225
    v = 100
    s = 20
    cd = 0.10

    mass = 5000
    g = 9.81
    thrust = 7000
    drag_force = 5000

    velocity_0 = 50
    acceleration_input = 2
    time = 10

    # Calculations
    range_ = calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed)
    endurance = calculate_endurance(fuel_capacity, fuel_consumption_rate)
    total_weight = calculate_total_weight(payload, fuel_weight)
    cg_position = calculate_cg_position(moment_list, total_weight_input)
    lift = calculate_lift(cl, rho, v, s)
    drag = calculate_drag(cd, rho, v, s)
    weight = calculate_weight(mass, g)
    acceleration = calculate_acceleration(thrust, drag_force, mass)
    velocity = calculate_velocity(velocity_0, acceleration, time)
    distance = calculate_distance(velocity, time)
    ld_ratio = calculate_ld_ratio(lift, drag)

    # Store results
    results = {
        "Range (miles)": round(range_, 2),
        "Endurance (hours)": round(endurance, 2),
        "Total Weight (lb)": total_weight,
        "CG Position (ft)": round(cg_position, 4),
        "Lift (N)": round(lift, 2),
        "Drag (N)": round(drag, 2),
        "Weight (N)": round(weight, 2),
        "Acceleration (m/s^2)": round(acceleration, 2),
        "Velocity (m/s)": round(velocity, 2),
        "Distance (m)": round(distance, 2),
        "Lift-to-Drag Ratio": round(ld_ratio, 2)
    }

    pretty_print(results)
    save_to_file(results)

if __name__ == "__main__":
    main()
