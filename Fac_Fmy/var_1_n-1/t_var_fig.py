import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('s_N100_Ae4_x0001e6_tmax10000.dat')
data2 = np.loadtxt('s_N100_Ae4_x001e6_tmax10000.dat')
data3 = np.loadtxt('s_N100_Ae4_x01e6_tmax10000.dat')
#data4 = np.loadtxt('s_N100_Ae4_x001e6_tmax10000.dat')
#data5 = np.loadtxt('change_kcon_20_070_ss_100.dat')
#data6 = np.loadtxt('change_kcon_20_080_ss_100.dat')
#data7 = np.loadtxt('change_kcon_20_090_ss_100.dat')
#data8 = np.loadtxt('change_kcon_20_100_ss_100.dat')

l1 = data1[:,0]
p1 = data1[:,3]

l2 = data2[:,0]
p2 = data2[:,3]

l3 = data3[:,0]
p3 = data3[:,3]

#l4 = data4[:,0]
#p4 = data4[:,3]

#l5 = data4[:,0]
#p5 = data4[:,1]

#l6 = data4[:,0]
#p6 = data4[:,1]

#l7 = data4[:,0]
#p7 = data4[:,1]

#l8 = data4[:,0]
#p8 = data4[:,1]

fig, axe = plt.subplots(1, 1)

axe.plot(l1, p1, 'o-', c='black', label = r'$x_{0}=10^{-9}$')#'$k_{on}^{c}=2,k_{off}=0.2$')
axe.plot(l2, p2, 's-', c='red', label = r'$x_{0}=10^{-8}$')#'$k_{on}^{c}=5,k_{off}=0.2$')
axe.plot(l3, p3, 'v-', c='blue', label = r'$x_{0}=10^{-7}$')#'$k_{on}^{c}=10,k_{off}=0.2$')
#axe.plot(l4, p4, '-p',  c='green', label =r'$N=200$')#'$k_{on}^{c}=20,k_{off}=0.2$')
plt.xlabel("time", fontsize = 18)
#plt.ylabel("Percolatin Probability", fontsize = 18)
plt.ylabel("variance", fontsize = 18)
#plt.ylim(0, 1.1)
#plt.xlim(0, 30)

axe.legend(loc='best')
fig.savefig("fig_t_var_x0_N100_Ae4_tmax10000.png")
#plt.show()
