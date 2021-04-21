# Importing the needed python packages
import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import time 
import sys
from pylab import *
from matplotlib.patches import Rectangle
# biological parameters definition
kdim=1
kdiss=1
Dp=0.1
Dpp=0.01
N=1000 # number of proteins P on the grid at the initial time
# simulation parameters:
systemsizeX=1 # length of the patch of membrane along the X axis
systemsizeY=1 # length of the patch of membrane along the Y axis
NpointX=100 # number of grid points along the X axis
NpointY=100 # number of grid points along the Y axis
hX=systemsizeX/NpointX
hY=systemsizeY/NpointY
timemax=20
# renormalization of diffusion coefficients:
DpX=Dp/hX/hX
DpY=Dp/hY/hY
DppX=Dpp/hX/hX
DppY=Dpp/hY/hY

# definition of the stochastic variables P and PP at all the grid points
P=np.zeros([NpointX,NpointY])
PP=np.zeros([NpointX,NpointY])
# definition of the propensity matrices A1, A2, A3... A10 ... that contains the propensities of the reactions 1, 2, 3 ... at all surface elements (i,j)
A1=np.zeros([NpointX,NpointY])
A2=np.zeros([NpointX,NpointY])
A3=np.zeros([NpointX,NpointY])
A4=np.zeros([NpointX,NpointY])
A5=np.zeros([NpointX,NpointY])
A6=np.zeros([NpointX,NpointY])
A7=np.zeros([NpointX,NpointY])
A8=np.zeros([NpointX,NpointY])
A9=np.zeros([NpointX,NpointY])
A10=np.zeros([NpointX,NpointY])

# Initialization distribute the N proteins P randomly across the grid
for n in range(0,N):
    # we randomly pick the row and column index of the surface element in which we place one of the N proteins
    i=randint(1,100) 
    j=randint(1,100)
    P[i][j]=P[i][j]+1


# simulation of time evolution
while Times[-1]<timemax:
    # first we calculate the propensity matrices A1, A2, A3... A10 ... that contains the propensities of the reactions 1, 2, 3 ... at all surface elements (i,j)
    for i in range(0,NpointX):
        for j in range(0,NpointY):
            A1[i][j]=kdim/2*P[i][j]*(P[i][j]-1)
            A2[i][j]=kdiss*PP[i][j]
            A3[i][j]=DpX*P[i][j]
            A5[i][j]=DpY*P[i][j]
            A7[i][j]=DppX*PP[i][j]
            A9[i][j]=DppY*PP[i][j]
    for i in range(0,NpointX-1):
        for j in range(0,NpointY):
            A4[i][j]=DpX*P[i+1][j]
            A8[i][j]=DppX*PP[i+1][j]
    for i in range(0,NpointX):
        for j in range(0,NpointY-1):
            A6[i][j]=DpY*P[i][j+1]
            A10[i][j]=DppY*PP[i][j+1]

    # we compute the total propensity by summing over all elements
    atot=sum(A1)+sum(A2)+sum(A3)+sum(A4)+sum(A5)+sum(A6)+sum(A7)+sum(A8)+sum(A9)+sum(A10)
    # generate random number r1 and pick the date of next reaction
    r1=np.random.uniform(0,1, size=None)
    nexttime=Times[-1]+np.log(1/r1)/atot
    Times.append(nexttime)
    # generate random number r2 and pick the type of the next reaction; also update the values of S, I, and R to the next time point
    r2=np.random.uniform(0,1, size=None)
    



TO BE COMPLETED: FAUT QUE J'ETENDE UNE DIMENSION DE PLUS DANS LES ARRAYS POUR AVOIR LE TIMECOURSE ET C'EST TROP LONG





# plotting the results
plt.figure()
plt.plot(Times,S,'-')
plt.plot(Times,I,'--')
plt.plot(Times,R,'.-')
plt.show()

