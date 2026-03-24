#  Aircraft Performance Calculator

This project is a Python-based tool developed for preliminary aircraft performance analysis. It evaluates key flight parameters such as range, endurance, lift, drag, and longitudinal dynamics.

##  Features

- Range and endurance estimation  
- Lift and drag calculation  
- Weight and center of gravity evaluation  
- Acceleration, velocity, and distance computation  
- Lift-to-drag (L/D) ratio analysis  

##  Methodology

The model is based on simplified aerodynamic and flight mechanics equations:

- Lift = 0.5 * CL * rho * V² * S  
- Drag = 0.5 * CD * rho * V² * S  
- Weight = m * g  
- Acceleration = (Thrust - Drag) / Mass  

Assuming steady level flight, vertical forces are balanced (Lift ≈ Weight), and acceleration is computed along the longitudinal axis.

## Example Results

- Range: 3000 miles  
- Endurance: 20 hours  
- Lift: 183750 N  
- Drag: 12250 N  
- Lift-to-Drag Ratio: 15  
- Acceleration: 0.4 m/s²

##  Engineering Insight

The model demonstrates how aerodynamic efficiency (L/D ratio) and thrust-to-drag balance directly influence aircraft acceleration and overall performance.

By adjusting input parameters, different flight conditions can be simulated, making this tool useful for preliminary design analysis.

##  Notes

This model uses simplified assumptions and constant parameters. Results are intended for educational and preliminary engineering analysis.

##  Technologies

- Python  
- NumPy  

##  Future Improvements
 
- Include mission profiles  
- Introduce user input interface  

##  Author

Simone Muscolino  
Aerospace Engineering Student
