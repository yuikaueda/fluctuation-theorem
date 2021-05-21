import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = np.loadtxt('sarcomerelength.dat')
df1 = df.round(2)



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ret = ax.hist(df1, bins=17, density=True, range=(0.35,3.75), histtype='barstacked', ec='black')
#ret1 = list(ret)
#ret1[0] = ret1[0]/491
print(ret[1])
#file = open('hist_data.dat','w')
#file.writelines(str(ret))
#file.close()

plt.xlabel(r"$sarcomere\ length[\mu m]$", fontsize = 18)
plt.ylabel(r"$PDF$", fontsize = 18)
fig.savefig("hist_round1_bin18")
plt.show()
