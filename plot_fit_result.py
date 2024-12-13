import numpy as np
import matplotlib.pyplot as plt 

L_pulseheight_mV = []
L_pulseheight_keV = []
L_counts = []

a = 0.436571757864683
b = 4.186197448725668

# relation: mv = a * keV + b, keV = mV - b / a

row_count = 0 
with open('Last_day_spectrum_Watch_HPGe.csv', 'r') as spectrum:
    for row in spectrum:
        if row_count > 0:
            data_splitted = row.split(',')

            L_pulseheight_mV.append(float(data_splitted[0]))
            pulseheight_eV = (float(data_splitted[0]) - b) / a
            L_pulseheight_keV.append(pulseheight_eV)

            L_counts.append(float(data_splitted[1]))
        row_count+=1 

plt.plot(L_pulseheight_mV, L_counts, color = 'RoyalBlue')
plt.xticks(np.arange(0,1000, 100))
plt.xlabel('Pulseheight (mV)')
plt.ylabel('Counts')
plt.show()