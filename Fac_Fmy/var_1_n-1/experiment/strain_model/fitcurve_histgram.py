import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
from scipy.optimize import curve_fit
from lmfit.models import GaussianModel
from lmfit.lineshapes import gaussian

df = np.loadtxt('sarcomerelength.dat')
df1 = df.round(2)


a,b = np.histogram(df1, bins=10, density=True, range=(0.35,3.75))
#plt.close()

x = []
y = []

b_ini = -0.025
for i in range(0, 2):
    y.append(a[i])
    x.append(b_ini)
    b_ini += 0.025

step = 0
for i in range(2, 10):
    y.append(a[9-step])
    x.append(b_ini)
    b_ini += 0.025
    step += 1

x=np.array(x)
y=np.array(y)
gauss1 = GaussianModel(prefix='g1_')
pars = gauss1.guess(y, x)
#pars.update(gauss1.make_param1())
pars['g1_center'].set(value=0.0, min=-0.001, max=0.001)
pars['g1_sigma'].set(value=0.07, min=0.001)
pars['g1_amplitude'].set(value=0.01, min=0.0001)
pars['g1_height'].set(value=0.4, max=0.5)

gauss2 = GaussianModel(prefix='g2_')
pars.update(gauss2.make_params())
pars['g2_center'].set(value=0.2, min=0.18, max=0.21)
pars['g2_sigma'].set(value=0.1, min=0.01)
pars['g2_amplitude'].set(value=0.9, min=0.01)

mod = gauss1 + gauss2

init = mod.eval(pars, x=x)

out = mod.fit(y, pars, x=x)

print(out.fit_report())
print(out.best_values['g1_center'])

x_max = x.max()
x_min = -x_max

x_new = np.linspace(x.min(),x.max(),1000)
smmoth_gauss = gaussian(x_new, amplitude=out.best_values['g1_amplitude'], center=out.best_values['g1_center'], sigma=out.best_values['g1_sigma'])+gaussian(x_new, amplitude=out.best_values['g2_amplitude'], center=out.best_values['g2_center'], sigma=out.best_values['g2_sigma'])

fig, ax = plt.subplots(1, 1)
ax.scatter(x, y, s=5, label = r'data')
#ax.plot(x, out.best_fit, 'r-')
ax.plot(x_new, smmoth_gauss, "-", c='red', label = r'gaussian fitting')
#ax.bar(x, y, width=0.025, edgecolor="#000000")
ax.legend()
plt.xlabel(r"$sarcomere\ length[\mu m]$", fontsize = 18)
plt.ylabel(r"$PDF$", fontsize = 18)
fig.savefig("fitcurve_strainhist_round2_bin10")
plt.show()
