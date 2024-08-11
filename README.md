# Intro
We were working with Vertex 80v FTIR made by Bruker.
The system works with OPUS software from bruker.

## Script
Additional script ascii_convert.py is a prototype, it converts OPUS spectra files into CSV files that can be used as input for analysing tools such as ENVI.

## Funtions
The code contains two funtions
- file_prop - returns the spectra file properties.
- plot_spec - plots data from the spectra file, extra utility can convert wavenumber to wavelength and multiply the whole spectra sile so that its easier to compare.
- data_plot - plots data from spectra file, Used to get plots for the report.
- peak_shift_plot - this srcipt was used to plot the peak shifting data.
