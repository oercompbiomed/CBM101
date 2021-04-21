# Importing the needed python packages
import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import time 
import sys
from pylab import *
from matplotlib.patches import Rectangle
# Defining the right hand side of the ODEs (rate of changes of predator and prey)

def PredatorPrey(Population, t, r, a, b, d, pmax):
   
    dx = Population[0]*(r*(1-Population[0]/pmax)-a*Population[1])
    dy = Population[1]*(b*Population[0]-d)
    
    return np.array((dx,dy))



r = 7.0 # intitalization of the 4 parameters
a = 2.0
b = 1.5
d = 3.0
pmax = 5
coords = np.linspace(0,5,11)
X, Y = np.meshgrid (coords, coords)
Vx, Vy = PredatorPrey((X,Y), 0, r, a, b, d, pmax)
p=plt.quiver(X,Y,Vx,Vy)
plt.xlabel('prey')
plt.ylabel('predator')
plt.title('Predator-prey phase portrait')