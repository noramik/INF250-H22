from spectral import *
import numpy as np
import matplotlib.pyplot as plt 
import skimage

hyperim = np.load("nmbu.npy")
wavelength = envi.read_envi_header('nmbu.hdr')['wavelength']
ww = [float(i) for i in wavelength]

# Function for band number closest to desired wavelength
def band_num(desired_ww, ww):
    l_min = 100 # Just a default number
    for ix, w in enumerate(ww):
        l = abs(desired_ww - w) # Finds the difference between desired wavelenght and the actual wavelength
        if l < l_min: # If the difference is smaller than l_min, it overwrites l_min and updates closest_ww
            l_min = l
            closest_ww = ix
    return closest_ww

bww = band_num(440, ww) # Band corresponding to blue wavelength
gww = band_num(535, ww) # Band corresponding to green wavelength
rww = band_num(645, ww) # Band corresponding to red wavelength
nirww = band_num(800, ww)
print(rww, gww, bww, nirww)


imshow(hyperim, (rww, gww, bww), stretch=((0.02,0.98),(0.02,0.98),(0.02,0.98)))
plt.show()
plt.savefig("nmbu_rgb.png")


