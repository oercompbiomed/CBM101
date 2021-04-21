import matplotlib.pyplot as plt
import matplotlib.image as mpimg
print("The network could look like")
img = mpimg.imread('modelExercise2.png')
imgplot = plt.imshow(img)
plt.show()
print("or this")
img = mpimg.imread('modelExercise2bis.png')
imgplot = plt.imshow(img)
plt.show()
print("but irrespective of how we represent it, the ODE describing the dynamics will be")
from IPython.display import display, Latex
display(Latex('$ dS_{phos}/dt = (k*S_0) * A(t) * (1-S_{phos}/S_0)$'))
