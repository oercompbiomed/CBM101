from IPython.display import display, Latex, Math

print("Reporting the particular form Phi(xi-c*tau) in the renormalized logistic PDE, we obtain the following equation on the function Phi, which is simply an ODE because Phi is by definition a function of a single variable. Let us denote z this variable:")

display(Latex('$d^2\Phi/dz^2 +c*d\Phi/dz+\Phi*(1-\Phi)=0,$'))
print("where")
display(Latex('$d^2\Phi/dz^2$'))
print("is the second derivative of Phi, and")
display(Latex('$d\Phi/dz$'))
print("the first derivative of Phi with respect to its (unique) variable. Of course, to get biological insight at some point we'll get to write explicitly that this variable depends on both space and time though z=xi-c*tau. But to solve the mathematical equations, we don't need to, rather we keep things as simple as possible. The equation is a second order ODE. We have seen that one convenient way to tackle such equations was to express it as a system of 2 coupled first order ODEs, where one variable is the unknown function Phi and the second one, its derivative:")
print("")
print("Hence, we denote Psi=Phi':")
display(Latex('$\Psi=d\Phi/dz$'))
print("therefore")
display(Latex('$d^2\Phi/dz^2=d\Psi/dz$'))
print("and the original second order ODE becomes a system of two coupled first order ODEs for Phi and Psi:")

display(Latex('$ d\Psi/dz= - c*\Psi-\Phi*(1-\Phi)=0$'))
display(Latex('$d\Phi/dz = \Psi$'))

print("Then, to get better semi-quantitative insight on the dynamical behavior of the system, we could represent the phase portrait for different values of the parameter c. We note that the biologically acceptable values of Phi are such that 0<=Phi(z)<=1, because those biological variables are positive and the carrying capacity (maximal population) of the renormalized Logistic PDE is 1. Hence, the phase portrait shall be plotted for 0=<Phi<=1, the values of Psi being a priori unrestricted.")
print("Doing so, we will obtain restrictions on the parameter c for which the system might converge to biologically acceptable solutions.")
print("Hence, we will obtain a range of acceptable velocity c for which a traveling wave at velocity c might solve the logistic PDE problem, given a set of boundary conditions and/or initial conditions.")
print("This does not preclude, however, the existence of other types of solutions. Traveling waves re frequently observed in space-dependent Lotka-Volterra models (similar to logistic) for predator prey interactions in nature.")
print("The complete resolution of this in C.J.H. Jonkhout's bachelor thesis available to download here:  https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjAn-Hlv77uAhWFl4sKHWW7BigQFjAAegQIARAC&url=https%3A%2F%2Fwww.universiteitleiden.nl%2Fbinaries%2Fcontent%2Fassets%2Fscience%2Fmi%2Fscripties%2Fjonkhout.pdf&usg=AOvVaw3HoUigDUpSD3ZtsA-3aktM  . ")
