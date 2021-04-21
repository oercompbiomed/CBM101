import numpy as np
import matplotlib.pyplot as plt


# plot Pc, Ppic, Pe, Pp as a function of k3 with k1, k2 fixed
k1 = 4
k2 = 4
k3=[]
Pc=[]
Ppic=[]
Pe=[]
Pp=[]
for i in range(0,2000):
    k3.append(i*0.01)
    Pc.append(1/(1+k1+k1*k2+k1*k2*k3[-1]));
    Ppic.append(k1/(1+k1+k1*k2+k1*k2*k3[-1]));
    Pe.append(k1*k2/(1+k1+k1*k2+k1*k2*k3[-1]));
    Pp.append(k1*k2*k3[-1]/(1+k1+k1*k2+k1*k2*k3[-1]));
plt.figure()
plt.plot(k3,Pc,'-',color='k')
plt.plot(k3,Ppic,'-',color='r')
plt.plot(k3,Pe,'-',color='b')
plt.plot(k3,Pp,'-',color='g')
plt.show()