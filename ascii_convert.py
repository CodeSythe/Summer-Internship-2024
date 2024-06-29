from brukeropusreader import read_file
import pandas as pd
import matplotlib.pyplot as plt

filepath = r'Nir comparison\NIR-comp-TRANS\PUG-18-5_trans-ref2-(old_ref)_VTX_NIR_202405311616.0'

data = read_file(filepath)

x = data.get_range()
y = data['AB'][0:len(x)]

df = pd.DataFrame(y,x)

df.to_csv('spec_export.csv')
print('spectra extracted to a CSV file')

#df.plot()
#plt.show()

#print(df)