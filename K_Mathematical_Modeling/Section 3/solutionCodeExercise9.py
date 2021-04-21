# Importing the needed python packages
import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import time 
import sys
from pylab import *
from matplotlib.patches import Rectangle
# biological parameters definition
b=1
beta=0.1
alpha=0.1
muS=0.01
muR=0.01
muI=0.1


# Initialization
timemax=20
Times=[0]
S=[99]
I=[1]
R=[0]

# simulation of time evolution
while Times[-1]<timemax:
    # total propensity:
    atot=b+muS*S[-1]+beta*S[-1]*I[-1]+muI*I[-1]+alpha*I[-1]+muR*R[-1]
    # generate random number r1 and pick the date of next reaction
    r1=np.random.uniform(0,1, size=None)
    nexttime=Times[-1]+np.log(1/r1)/atot
    Times.append(nexttime)
    # generate random number r2 and pick the type of the next reaction; also update the values of S, I, and R to the next time point
    r2=np.random.uniform(0,1, size=None)
    if r2*atot<b:
        # then we pick the reaction: birth of an individual; S is increased by one unit, I and R are unchanged
        S.append(S[-1]+1)
        I.append(I[-1])
        R.append(R[-1])
    elif r2*atot<b+muS*S[-1]:
        # then we pick the reaction: death of a susceptible individual; S is decreased by one unit, I and R are unchanged
        S.append(S[-1]-1)
        I.append(I[-1])
        R.append(R[-1])
    elif r2*atot<b+muS*S[-1]+beta*S[-1]*I[-1]:
        # then we pick the reaction: infection of a susceptible individual; S is decreased by one unit, I increased by one unit, R unchanged
        S.append(S[-1]-1)
        I.append(I[-1]+1)
        R.append(R[-1])
    elif r2*atot<b+muS*S[-1]+beta*S[-1]*I[-1]+muI*I[-1]:
        # then we pick the reaction: death of an infected individual; I decreased by one unit, S and R unchanged
        S.append(S[-1])
        I.append(I[-1]-1)
        R.append(R[-1])
    elif r2*atot<b+muS*S[-1]+beta*S[-1]*I[-1]+muI*I[-1]+alpha*I[-1]:
        # then we pick the reaction: recovery of an infected individual; I decreased by one unit, R increased by one unit, S unchanged
        S.append(S[-1])
        I.append(I[-1]-1)
        R.append(R[-1]+1)
    else:
        # then we pick the last reaction, death of a recovered individual; R decreased by one unit, S and I unchanged
        S.append(S[-1])
        I.append(I[-1])
        R.append(R[-1]-1)


# plotting the results
plt.figure()
plt.plot(Times,S,'-')
plt.plot(Times,I,'--')
plt.plot(Times,R,'.-')
plt.show()

