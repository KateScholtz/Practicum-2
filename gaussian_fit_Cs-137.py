import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Gaussian function for fitting
def gaussian(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))


L_pulse_heights = []
L_counts = []

sum_counts_peak = 0
sum_counts = 0

row_count = 0 
with open('spectrum_Cs-137.csv', 'r') as spectrum_Cs_137:

    for row in spectrum_Cs_137:
        if row_count > 0:
            data_splitted = row.split(',')

            if float(data_splitted[0]) > 200 and float(data_splitted[0]) < 300:
                sum_counts_peak += float(data_splitted[1])
            sum_counts += float(data_splitted[1])

            L_pulse_heights.append(float(data_splitted[0]))
            L_counts.append(float(data_splitted[1]))

        row_count+=1 

pulse_heights = np.array(L_pulse_heights)
counts = np.array(L_counts)

# Fit the data to a Gaussian
initial_guess = [max(counts), pulse_heights[np.argmax(counts)], 10]  # Initial guess for A, mu, sigma
popt, pcov = curve_fit(gaussian, pulse_heights, counts, p0=initial_guess)

# Extract fitted parameters
A, mu, sigma = popt
fwhm = 2.355 * sigma  # Calculate FWHM from sigma

# Energy of the peak (for Cs-137, it’s 235 mV)
E_peak = 235

# Calculate resolution
resolution = (fwhm / E_peak) * 100

# Print results
print(f"Fitted peak center (mu): {mu} mV")
print(f"FWHM: {fwhm} mV")
print(f"Energy resolution: {resolution:.2f}%")

# Plot the data and fit
plt.plot(pulse_heights, counts, label="Data")
plt.plot(pulse_heights, gaussian(pulse_heights, *popt), label="Gaussian Fit", linestyle="--", color="red")
plt.xlabel("Pulseheight (mV)")
plt.ylabel("Counts")
plt.title(f"Photo-peak fit and resolution calculation\nResolution: {resolution:.2f}%")
plt.legend()
plt.show()

