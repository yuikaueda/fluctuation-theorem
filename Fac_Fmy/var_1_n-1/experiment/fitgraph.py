import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df = np.loadtxt('sarcomerelength.dat')
df1 = df.round(2) - 1.12
num = 20

a, b, _ = plt.hist(df1, bins=num, density=True)
plt.close()
#print(a)
aa = []
bb = []

step0=0
for i in range(0, 5):
    if not a[i] == 0 and not a[-i] == 0:
        a_hi = math.log(a[i]/a[i+12-step0])
        aa.append(a_hi)
        step0 += 2
        bb.append(b[i])
        #print(aa)
        #p = math.log(aa)

a_hi = math.log(a[6]/a[6])
aa.append(a_hi)
bb.append(b[6])

step=1
for i in range(7, 13):
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
fig.savefig("ln_st02_round2_fig_lnp_bins30")
#plt.show()
