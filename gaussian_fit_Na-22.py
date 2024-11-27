import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define a function with two Gaussian peaks
def double_gaussian(x, A1, mu1, sigma1, A2, mu2, sigma2):
    gauss1 = A1 * np.exp(-(x - mu1)**2 / (2 * sigma1**2))
    gauss2 = A2 * np.exp(-(x - mu2)**2 / (2 * sigma2**2))
    return gauss1 + gauss2


L_pulse_heights = []
L_counts = []

row_count = 0 
with open('spectrum_Na-22_HPGe.csv', 'r') as spectrum_Na_22_HPGe:
    for row in spectrum_Na_22_HPGe:
        if row_count > 0:
            data_splitted = row.split(',')
            L_pulse_heights.append(float(data_splitted[0]))
            L_counts.append(float(data_splitted[1]))
        row_count += 1

pulse_heights = np.array(L_pulse_heights)
counts = np.array(L_counts)

# Initial guesses for the two peaks
# A1, mu1, sigma1 for the first peak, A2, mu2, sigma2 for the second peak
initial_guess = [
    max(counts),  # A1
    pulse_heights[np.argmax(counts)],  # mu1
    10,  # sigma1
    max(counts) / 2,  # A2 (a smaller amplitude for the second peak)
    pulse_heights[np.argmax(counts) + 100],  # mu2 (shifted to another peak)
    10,  # sigma2
]

# Fit the data to the double Gaussian function
popt, pcov = curve_fit(double_gaussian, pulse_heights, counts, p0=initial_guess)

# Extract fitted parameters
A1, mu1, sigma1, A2, mu2, sigma2 = popt

# Calculate FWHM and resolution for each peak
fwhm1 = 2.355 * sigma1
fwhm2 = 2.355 * sigma2

# Define reference energies for each peak if known
E_peak1 = 511  # Example: Na-22 at 511 keV
E_peak2 = 1274  # Example: Na-22 at 1274 keV

resolution1 = (fwhm1 / E_peak1) * 100
resolution2 = (fwhm2 / E_peak2) * 100

# Print results for both peaks
print(f"Peak 1: mu = {mu1:.2f} mV, FWHM = {fwhm1:.2f} mV, Resolution = {resolution1:.2f}%")
print(f"Peak 2: mu = {mu2:.2f} mV, FWHM = {fwhm2:.2f} mV, Resolution = {resolution2:.2f}%")

# Plot the data and the fit
plt.plot(pulse_heights, counts, label="Data")
plt.plot(pulse_heights, double_gaussian(pulse_heights, *popt), label="Double Gaussian Fit", linestyle="--", color="red")

# Plot individual Gaussian components
plt.plot(pulse_heights, A1 * np.exp(-(pulse_heights - mu1)**2 / (2 * sigma1**2)), label="Peak 1", linestyle=":", color="blue")
plt.plot(pulse_heights, A2 * np.exp(-(pulse_heights - mu2)**2 / (2 * sigma2**2)), label="Peak 2", linestyle=":", color="green")

plt.xlabel("Pulseheight (mV)")
plt.ylabel("Counts")
plt.title("Double Gaussian Fit")
plt.legend()
plt.show()
