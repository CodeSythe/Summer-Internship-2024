from brukeropusreader import read_file
import pandas as pd
import matplotlib.pyplot as plt

filepath = r'GIR-objective_test_BNG-1-B_pellet_high-scans_HYP_MIR_202407241524.0'

data = read_file(filepath)

x = data.get_range('AB',wavenums=True)
y = data['AB'][0:len(x)]

#x = x/1000
y = y

plt.plot(x,y,'b')

plt.title('Spectra of BNG-1-B using the GIR objective on Hyperion')
plt.autoscale(axis='x',tight=True)
plt.grid(True,'both')

plt.xlabel(r'Wavelength ($cm^-1$)')
#plt.xlabel(r'Wavelength ($\mu$m)')
plt.ylabel('Reflection')

plt.show()
