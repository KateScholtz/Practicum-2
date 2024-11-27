import numpy as np
import matplotlib.pyplot as plt 
from lmfit import models

# Data
pulse_heights = np.array([227.27, 560.61])
energies = np.array([510.99, 1274.53])
errors_pulse_heights = np.array([18, 16])

# Define the function
def function(x, a, b):
    return (x * a + b)

# Model fitting
model = models.Model(function)
# Use weights (1 / errors) for fitting
weights = 1 / errors_pulse_heights
result = model.fit(pulse_heights, x=energies, weights=weights, a=1, b=100)

# Plotting
plt.errorbar(energies, pulse_heights, yerr=errors_pulse_heights, fmt='o', label='Data', capsize=5)
plt.plot(energies, result.best_fit, 'r-', label='Best fit')
plt.xlabel('Energies')
plt.ylabel('Pulse Heights')
plt.legend()
plt.show()

# Fit report and parameter errors
print(result.fit_report())
print("\nParameter Errors:")
for param_name, param in result.params.items():
    print(f"{param_name}: Value = {param.value}, Error = {param.stderr}")