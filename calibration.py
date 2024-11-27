import numpy as np
import matplotlib.pyplot as plt 
from lmfit import models

# Data
pulse_heights = np.array([227.3, 560.6])
energies = np.array([511, 1274.537])
errors_pulse_heights = np.array([227.3, 560.6])

# Define the function
def function(x, a, b):
    return (x * a + b)

# Model fitting
model = models.Model(function)
result = model.fit(
    pulse_heights,
    x=energies,
    weights=1 / errors_pulse_heights,  # Use weights as inverse of errors
    a=1, b=1
)

# Plotting
plt.plot(energies, result.best_fit, 'r-', label='Best fit')
plt.plot(energies, pulse_heights, 'o', label='Data')
plt.xlabel('Energies')
plt.ylabel('Pulse Heights')
plt.legend()
plt.show()

# Fit report and parameter errors
print(result.fit_report())
print("\nParameter Errors:")
for param_name, param in result.params.items():
    print(f"{param_name}: Value = {param.value}, Error = {param.stderr}")
