import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit

df = np.loadtxt('sarcomerelength.dat')
df1 = df.round(1) - 1.12
num = 18

a, b, _ = plt.hist(df1, bins=num, range=(-0.9,2.6), density=True)
plt.close()
#print(a)
aa = []
bb = []

step0=0
for i in range(0, 4):
    #if not a[i] == 0 and not a[i+8-step0] == 0:
    a_hi = math.log(a[i]/a[i+8-step0])
    aa.append(a_hi)
    bb.append(b[i])
    step0+=2
        #print(aa)
        #p = math.log(aa)

a_hi = 0
aa.append(a_hi)
bb.append(0)

step=2
for i in range(5, 9):
    #if not a[i] == 0 and not a[i-step] == 0: 
    a_hi = math.log(a[i]/a[i-step])
    aa.append(a_hi)
    bb.append(b[i])
        #print(aa)
    step+=2

#print(aa)
#print(bb)

K=1.38e-23
T=309.5
def fit(x,F):
    return F*x/(K*T)

param, cov = curve_fit(fit, bb, aa)
print(param)

FF=param[0]*1e6

print(FF)

y_fit = []
for num in range(len(bb)):
    y_fit.append(param[0]*bb[num]/(K*T))
array_y_fit = np.array(y_fit)    
#print(aa)
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)

#ret = ax.hist(df1, bins=30, density=True, histtype='barstacked', ec='black')
#ret1 = list(ret)
#ret1[0] = ret1[0]/491

#file = open('hist_data.dat','w')
#file.writelines(str(ret))
#file.close()

fig, ax = plt.subplots(1, 1)
ax.plot(bb, aa, 'o', c='red')
ax.plot(bb, array_y_fit, '-', c='black', label = r'$ln[P( \Delta x) / (- \Delta x)]= {:.3e}x/KT$'.format(FF) )
plt.xlabel(r"$sarcomere\ length[\mu m]$", fontsize = 18)
plt.ylabel(r"$ln[P( \Delta x) / P(- \Delta x)]$", fontsize = 18)
ax.legend()
fig.savefig("fitlnp_range_ln_st02_round1_bins18")
plt.show()
