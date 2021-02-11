from IPython.display import display, Latex
print("Yes, this model is sufficient. First thing to do is define kA and kB, the rates of vesicle emission by organelle A and B respectively per unit surface area of each organelle.")
print("Then, we can calculate the total rates fA and fB of vesicle emission by A and B, from their entire surface:")

display(Latex('$ f_A=k_A*S_A$'))
display(Latex('$ f_B=k_B*S_B$'))
print("where S_A and S_B are the total surfaces of each organelle. But since each vesicle takes with it a certain amount of membrane, that correspond to its surface area, these rates can be converted to rates of change of the total surface area of the organelles A and B and writing balance equations for the surfaces S_a and S_B we get the ODEs:")
display(Latex('$dS_A/dt = - k_A*S_A*(4*\pi * r_a^2) + k_B*S_B*(4*\pi * r_b^2)$'))
display(Latex('$dS_B/dt = + k_A*S_A*(4*\pi * r_a^2) - k_B*S_B*(4*\pi * r_b^2)$'))
print("Solving this system of ODEs with appropriate initial conditions will give us the time evolution of the surface areas of both organelles.")
