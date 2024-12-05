import numpy as np
import matplotlib.pyplot as plt 

L_pulseheight_mV = []
L_pulseheight_keV = []
L_counts = []

a = 0.43657176
b = 4.18619745

row_count = 0 
with open('spectrum_Mushrooms_HPGe.csv', 'r') as spectrum_Cs_137:
    for row in spectrum_Cs_137:
        if row_count > 0:
            data_splitted = row.split(',')

            L_pulseheight_mV.append(float(data_splitted[0]))
            # pulseheight_eV = a * float(data_splitted[0]) + b
            pulseheight_eV = (float(data_splitted[0]) - b) / a
            L_pulseheight_keV.append(pulseheight_eV)

            L_counts.append(float(data_splitted[1]))
        row_count+=1 

plt.fill_between(L_pulseheight_keV, L_counts, color='blue', alpha=0.8)
plt.plot(L_pulseheight_keV, L_counts, color = 'blue')
plt.xlabel('Pulseheight (keV)')
plt.ylabel('Counts')
plt.xlim(0,2000)  
plt.ylim(bottom=0)
plt.title("Spectrum of Mushrooms (Cs-137)")
plt.savefig("plot Cs-137.png")