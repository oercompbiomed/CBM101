from IPython.display import display, Latex, Math

print("If the kon1 and koff1 rates are much larger than kon2 and koff2, we can approximate the formation of the AB complex to be constantly at equilibrium. Thus we can do a quasi steady state approximation since we have time scale separation between fast rates, kon1, koff1, and slow rates, kon2 and koff2. ")
print("As discussed above, we have the choice. We can first assume that d[B]/dt=0 (d[A]/dt, in contrast, has a slow component).")
print("The equations become:")
display(Latex('$d[AB]/dt = - k_{on2}*[A]*[AB] + k_{off2}*[A_2B]$'))
display(Latex('$d[A_2B]/dt = k_{on2}*[A]*[AB] - k_{off2}*[A_2B]$'))
display(Latex('$d[A]/dt = - k_{on2}*[A]*[AB] + k_{off2}*[A_2B]$'))
display(Latex('$d[B]/dt = 0$'))
display(Latex('$[A]+[AB]+2*[A_2B] = A_0$'))
display(Latex('$[B]+[AB]+[A_2B] = B_0$'))

print("We note that the equations above imply that d([AB]+[A_2B])=0 and that d([A]+[A_2B])=0. Hence,[AB]+[A_2B] and [A]+[A_2B] are two constants in time. Let's call C the first one: [AB]+[A_2B]=C, constant, which is no more no less than the total concentration of protein B that is trapped in complex form.")
print("We have then: ")

display(Latex('$[B] = B_0 - C$'))
display(Latex('$[A_2B] = A_0 - C - [A]$'))
display(Latex('$[AB] = B_0-[B]-[A_2B]=2*C- A_0  + [A]$'))

print("and the entire system reduces to just one ODE for [A]")
display(Latex('$ d[A]/dt = - k_{on2}*[A]*(2*C- A_0  + [A]) + k_{off2}*(A_0 - C - [A])$'))
print("in which we can reorder the right hand side to make successive powers of [A] more explicit: ")

display(Latex('$ d[A]/dt = - k_{on2}*[A]^2 - (k_{on2}*(2*C- A_0)+k_{off2})*[A]+ k_{off2}*(A_0 - C)$'))

print("On the right hand side, we have a second order polynomial in A. You know from high-school how to compute the roots A1 and A2, using the discriminant, and thus how to factorise it in the form -kon2*(A-A1)*(A-A2). Then, the ODE can be rewritten as dA/((A-A1)*(A-A2))=-kon2*dt (separation of variables), from which the partial fraction decomposition shall be used to integrate both sides separately and find the general solution A(t). This technique is detailed earlier in this section of the notebook.")

print("Once we have chosen the initial conditions, the solution we find will depend on the constant C, and the parameters A_0, B_0, kon2 and koff2. Thus, the behavior of the system at large times will explicitly depend on the constant C. However, because we (should) have been able to compute exactly the steady state of the full ODE system (remember: the equations defining the Kds of both complexes), and thus to commpute the equilibrium concentrations of all biological variables A, B, AB and A_2B, there is no room here for flexibility: the steady state is fully determined. This provides a way to compute the constant C. We don't want to overload this course with (basic) calculations, rather to focus on new concepts, but this is a good exercise to do. ")
print("")
print("Train yourself by computing the constant C as a function of A_0, B_0, and the rates!")
print("The QSSA and its unknown constant C has made our lives simpler, providing a convenient framework to obtain the full dynamics. However, we need to keep in mind that in general we know the initial conditions (because they depend on how we set up an experiment, so we kind of choose them), and the final conditions because in general we can readily compute the steady state. Thus, QSSA-like constants shall be eventually calculated.")

print("We note that another QSSA can be implemented: the assumption that fast forming intermediate species are always at equilibrium. Here, it is the complex AB. Type the command %run solutionODEsExercise14bis.py in a code cell to display this way of solving the problemm.")

