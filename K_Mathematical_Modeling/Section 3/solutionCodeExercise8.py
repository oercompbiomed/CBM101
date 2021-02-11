
# Importing the needed python packages
import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import time 
import sys
from pylab import *
from matplotlib.patches import Rectangle
# biological parameters definition
kon=0.1
koff=0.5
T=0.01
# simulation parameters definition
N=100 # number of timepoints
tmax=T*N # final time
nA = np.zeros(N+1)
nB = np.zeros(N+1)
nAB = np.zeros(N+1)
Times = np.zeros(N+1)
for i in range(0,N):  # Python starts indexing rows and columns at 0, not 1 as in the algorithm above
        Times[i] = i*T
# initialization
nA[0]=95
nB[0]=76
nAB[0]=0
# simulation of time evolution
for i in range(0,N):
    # reaction rates in the state at time t
    w1=kon*nA[i]*nB[i]
    w2=koff*nAB[i]
    # generate random number of reactions following the Poisson distribution
    n1=np.random.poisson(w1*T, size=None)
    n2=np.random.poisson(w2*T, size=None) 
    # compute right hand sides:
    DeltaN=-w1*T  + w2*T-n1 + n2
    nA[i+1]=nA[i]+DeltaN
    nB[i+1]=nB[i]+DeltaN
    nAB[i+1]=nAB[i]-DeltaN


# plotting the results
plt.figure()
plt.plot(nA,'-')
plt.plot(nB,'--')
plt.plot(nAB,'.-')
plt.show()

