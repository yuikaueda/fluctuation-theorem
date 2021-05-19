import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df = np.loadtxt('sarcomerelength.dat')
df1 = df.round(1) - 1.12
num = 18

a, b, _ = plt.hist(df1, bins=num, range=(-0.9,2.6), density=True)
plt.close()
#print(a)
aa = []
bb = []

step0=0
for i in range(0, 3):
    if not a[i] == 0 and not a[i+8-step0] == 0:
        a_hi = math.log(a[i]/a[i+8-step0])
        aa.append(a_hi)
        bb.append(b[i])
    step0+=2
        #print(aa)
        #p = math.log(aa)

a_hi = 0
aa.append(a_hi)
bb.append(b[4])

step=2
for i in range(5, 8):
    if not a[i] == 0 and not a[i-step] == 0: 
        a_hi = math.log(a[i]/a[i-step])
        aa.append(a_hi)
        bb.append(b[i])
        #print(aa)
    step+=2

print(aa)
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)

#ret = ax.hist(df1, bins=30, density=True, histtype='barstacked', ec='black')
#ret1 = list(ret)
#ret1[0] = ret1[0]/491

#file = open('hist_data.dat','w')
#file.writelines(str(ret))
#file.close()

fig, ax = plt.subplots(1, 1)
ax.plot(bb, aa, 'o', c='black')
plt.xlabel(r"$sarcomere\ length[\mu m]$", fontsize = 18)
plt.ylabel(r"$ln[P( \Delta x) / P(- \Delta x)]$", fontsize = 18)
fig.savefig("range_ln_st02_round1_fig_lnp_bins18")
plt.show()
