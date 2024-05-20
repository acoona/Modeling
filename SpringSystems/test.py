import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
m = 1.0  # Mass (kg)
k = 10.0  # Spring constant (N/m)
x0 = 1.0  # Initial displacement (m)
v0 = 0.0  # Initial velocity (m/s)

# Time span
t_span = (0, 10)  # Time range for the solution
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Time points where the solution is evaluated

# Define the system of differential equations
def spring_mass_system(t, y):
    x, v = y
    dxdt = v
    dvdt = - (k / m) * x
    return [dxdt, dvdt]

# Initial conditions: [initial displacement, initial velocity]
y0 = [x0, v0]

# Solve the ODE
solution = solve_ivp(spring_mass_system, t_span, y0, t_eval=t_eval)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(solution.t, solution.y[0], label='Displacement (x)')
plt.plot(solution.t, solution.y[1], label='Velocity (v)')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.title('Spring-Mass System')
plt.legend()
plt.grid()
plt.show()