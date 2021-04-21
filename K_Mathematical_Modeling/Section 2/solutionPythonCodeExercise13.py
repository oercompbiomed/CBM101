# Importing the needed python packages
import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import time 
import sys
from pylab import *
from matplotlib.patches import Rectangle
# Defining the right hand side of the ODEs (rate of changes of predator and prey)

def TrimolecularComplex(A,A2B,Kon1,Koff1,Kon2,Koff2,A0,B0):
   
    dA = - Kon1*A*(B0-A0+A+A2B) + Koff1 *(A0-A-2*A2B)- Kon2*A*(A0-A-2*A2B) + Koff2*A2B
    dA_2B = Kon2*A*(A0-A-2*A2B) - Koff2*A2B
    
    
    return np.array((dA,dA_2B))

Kon1 = 1
Koff1 = 1
Kon2 = 1
Koff2 = 1
A0 = 3
B0 = 1

coords = np.linspace(0,2,21)
X, Y = np.meshgrid (coords, coords)
Vx, Vy = TrimolecularComplex(A,A2B,Kon1,Koff1,Kon2,Koff2,A0,B0)
p=plt.quiver(X,Y,Vx,Vy)
plt.xlabel('conc. A')
plt.ylabel('conc. A_2B')
plt.title('Trimolecular complex formation phase portrait')