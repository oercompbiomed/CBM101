# Importing the needed python packages
import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import time 
import sys
from pylab import *
from matplotlib.patches import Rectangle
# Defining the right hand side of the ODEs (rate of changes of predator and prey)

def NegativeFBmodel(A,B,kAB,kBA):
   
    dA = 1-kBA*B
    dB = kAB*A
    
    return np.array((dA,dB))


kAB = 1
kBA = 1

coords = np.linspace(-5,5,21)
X, Y = np.meshgrid (coords, coords)
Vx, Vy = NegativeFBmodel(X,Y,kAB,kBA)
p=plt.quiver(X,Y,Vx,Vy)
plt.xlabel('conc. A')
plt.ylabel('conc. B')
plt.title('Linear negative feedback phase portrait')