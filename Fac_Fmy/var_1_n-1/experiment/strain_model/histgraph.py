import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df = np.loadtxt('sarcomerelength.dat')
df1 = df.round(2)


a,b, _ = plt.hist(df1, bins=10, density=True, range=(0.35,3.75), histtype='barstacked', ec='black')
plt.close()

aa = []
bb = []

b_ini = -0.025
for i in range(0, 2):
    aa.append(a[i])
    bb.append(b_ini)
    b_ini += 0.025

step = 0
for i in range(2, 10):
    aa.append(a[9-step])
    bb.append(b_ini)
    b_ini += 0.025
    step += 1

fig, ax = plt.subplots(1, 1)
ax.bar(bb, aa, width=0.025, edgecolor="#000000")
plt.xlabel(r"$\varepsilon$", fontsize = 18)
plt.ylabel(r"$PDF$", fontsize = 18)
fig.savefig("strainhist_round2_bin10")
plt.show()
