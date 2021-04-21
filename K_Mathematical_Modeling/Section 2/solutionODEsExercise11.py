from IPython.display import display, Latex, Math

print("If the resources are limited for the preys to grow, their effective reproduction rate will diminish with an increasing population of preys.")
print("We can account for this limited support of the environment by multiplying the prey reproduction rate by (1-preys/pmax) where pmax is the maximal population of preys that can be sustained by the environment (hence, when preys reaches pmax, reproduction rate falls to 0):")


display(Latex('$ dA/dt = r*A(t)*(1-A(t)/pmax)-a*A(t)*B(t)$'))

print("and the equation for the predators population [B] is unchanged:")

display(Latex('$ dB/dt =  -d*B(t)+b*A(t)*B(t)$'))

