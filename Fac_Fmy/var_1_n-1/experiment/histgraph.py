import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = np.loadtxt('sarcomerelength.dat')
df1 = df.round(1)



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ret = ax.hist(df1, bins=30, density=True, histtype='barstacked', ec='black')
#ret1 = list(ret)
#ret1[0] = ret1[0]/491

#file = open('hist_data.dat','w')
#file.writelines(str(ret))
#file.close()

plt.xlabel(r"$sarcomere\ length[\mu m]$", fontsize = 18)
plt.ylabel(r"$PDF$", fontsize = 18)
fig.savefig("kizyunn_round1_fig_bins30")
#plt.show()
