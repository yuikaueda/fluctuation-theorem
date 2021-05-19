import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit


df = np.loadtxt('sarcomerelength.dat')
df1 = df.round(1) - 1.12


hist_1, bins = np.histogram(df1, bins=15, density=True)
bins = bins[:-1]

def func(x, a, mu, sigma):
    return a*np.exp(-(x-mu)**2/(2*sigma**2))
param_ini = [1,0.001,1]
popt, pcov = curve_fit(func, bins, hist_1, p0=param_ini)
print(popt)

fitting = func(bins, popt[0], popt[1], popt[2])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.bar(bins, hist_1, width=0.22, alpha=0.5, color='blue', align='edge')
ax.plot(bins,fitting,'k')

plt.xlabel(r"$sarcomere\ length[\mu m]$", fontsize = 18)
plt.ylabel(r"$PDF$", fontsize = 18)
#fig.savefig("kizyunn_strain02_round1_fig_bins30")
plt.show()
