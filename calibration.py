import numpy as np
import matplotlib.pyplot as plt 
from lmfit import models

# Data
pulse_heights = np.array([227.27, 560.61])
energies = np.array([510.99, 1274.53])

# Define the function
def function(x, a, b):
    return (x * a + b)

# Model fitting
model = models.Model(function)
# Provide initial guesses
result = model.fit(pulse_heights, x=energies, a=0.5, b=100)

# Plotting
plt.plot(energies, pulse_heights, 'o', label='Data')
plt.plot(energies, result.best_fit, 'r-', label='Best fit')
plt.xlabel('Energies')
plt.ylabel('Pulse Heights')
plt.legend()
plt.show()

# Fit report and parameter values
print(result.fit_report())
