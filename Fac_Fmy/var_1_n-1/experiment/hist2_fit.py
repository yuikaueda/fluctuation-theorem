import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit
from lmfit.models import GaussianModel

df = np.loadtxt('sarcomerelength.dat')
df1 = df.round(1) - 1.12


hist_1, bins_1 = np.histogram(df1, bins=15, density=True)
bins = bins_1[:-1]

model = GaussianModel()
params = model.guess(hist_1, x=bins_1[1:])
result = model.fit(hist_1, params, x=bins_1[1:])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#ax.bar(bins, hist_1, width=0.11, alpha=0.5, color='m', align='edge')
#ax.plot(bins_1, result[0], 'k--')
result.plot_fit()
#ax.plot(bins_1[1:], result.init_fit, 'k--')

plt.xlabel(r"$sarcomere\ length[\mu m]$", fontsize = 18)
plt.ylabel(r"$PDF$", fontsize = 18)
#fig.savefig("kizyunn_strain02_round1_fig_bins30")
plt.show()
