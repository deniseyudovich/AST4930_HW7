import astropy as ast
from astropy import units as u
import numpy as np
import matplotlib.pyplot as plt


#read sed.txt and create array from data
text_file = open("sed.txt", "r")
sed = np.loadtxt('sed.txt', delimiter = ",")
wave = sed[:, 0]    
lum = sed[:, 1]     
print("wave: ", wave)
print("lum: ", lum)


#Create new array of x (wavelength) in specified distribution
b= np.where((wave<=1000) & (wave>=10))
newWave = np.array(wave[b])
#Create new arrat of y (luminosities) in the same index positions found from np.where()
newlum = np.array(lum[b])
output = np.trapz(newlum, -newWave)
#Convert units
output *= u.Lsun
output2 = output.to(u.erg/u.s)
print("output2: ", output2)




#Plot the spectral enegry distribution
plt.plot(wave, lum)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Wavelength (micron)')
plt.ylabel('Specific Luminosity (Lsun/micron)')
plt.savefig('yudovich_denise_hw7.png')

