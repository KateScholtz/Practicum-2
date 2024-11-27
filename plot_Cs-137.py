import numpy as np
import matplotlib.pyplot as plt 

L_pulseheight_mV = []
L_pulseheight_keV = []
L_counts = []

a = 0.0325
b = 196.826

row_count = 0 
with open('spectrum.csv', 'r') as spectrum_Cs_137:
    for row in spectrum_Cs_137:
        if row_count > 0:
            data_splitted = row.split(',')

            L_pulseheight_mV.append(float(data_splitted[0]))
            pulseheight_eV = a * float(data_splitted[0]) + b
            L_pulseheight_keV.append(pulseheight_eV)

            L_counts.append(float(data_splitted[1]))
        row_count+=1 

plt.plot(L_pulseheight_keV, L_counts)
plt.xlabel('Pulseheight (keV)')
plt.ylabel('Counts')
plt.show()