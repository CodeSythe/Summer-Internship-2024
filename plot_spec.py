#!usr/bin/python
from brukeropusreader import read_file
import matplotlib.pyplot as plt


def file_prop(file_path):                 #input - file path | return - Key values (name of stored data parameters)
    data = read_file(file_path)
    return data.keys()

def plot_spec(file_path,spec_name,multiplier=1,wn=True):
    data = read_file(file_path)
    if wn:                                #if input is True(default) - covert unit to nm | if input - False - unit stays cm^-1 
        x_ = 'Wavenumber (cm^(-1))'
    else:
        x_ = 'Wavelength (nm)'                      #x_ and y_ are just name for labels for the x and y axis
    if "AB" not in file_prop(file_path):            #Checks if file is a reference or sample spectra and loads the required data parameter 'AB' or 'ScRf'
        x = data.get_range('ScRf',wavenums=wn)
        r = data['ScRf'][0:len(x)]
        y = []
        for i in r:
            a = i*multiplier
            y.append(a)
        y_ = 'Intensity'
    else:
        x = data.get_range('AB',wavenums=wn)
        r = data['AB'][0:len(x)]
        y = []
        for i in r:
            a = i*multiplier
            y.append(a)
        y_ = 'Transmittance'
    
    plt.plot(x,y)
    plt.xlabel(x_)
    plt.ylabel(y_)
    plt.title(spec_name)
    plt.show()

spec = r'C:\Users\visha\OneDrive\Desktop\code\spectra\reflect_ref_day2_15_R.0'
plot_spec(spec,'test')