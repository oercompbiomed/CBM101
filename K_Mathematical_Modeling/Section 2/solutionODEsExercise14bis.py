from IPython.display import display, Latex, Math
print("Let's look again at the full ODE system:")

display(Latex('$ d[AB]/dt = k_{on1}*[A]*[B] - k_{off1}*[AB]- k_{on2}*[A]*[AB] + k_{off2}*[A_2B]$'))
display(Latex('$ d[A_2B]/dt = k_{on2}*[A]*[AB] - k_{off2}*[A_2B]$'))
display(Latex('$ d[A]/dt = - k_{on1}*[A]*[B] + k_{off1}*[AB]- k_{on2}*[A]*[AB] + k_{off2}*[A_2B]$'))
display(Latex('$ d[B]/dt = - k_{on1}*[A]*[B] + k_{off1}*[AB]$'))
display(Latex('$ [A]+[AB]+2*[A_2B] = A_0$'))
display(Latex('$ [B]+[AB]+[A_2B] = B_0$'))


print("The QSSA d[AB]=0 is equivalent to :")

display(Latex('$k_{on1}*[A]*[B] - k_{off1}*[AB] = k_{on2}*[A]*[AB] - k_{off2}*[A_2B]$'))

print("And using this identity, we can get rid of all the terms dependent on the fast rates in the ODEs, which become:")

display(Latex('$d[AB]/dt = 0$'))
display(Latex('$d[A_2B]/dt = k_{on2}*[A]*[AB] - k_{off2}*[A_2B]$'))
display(Latex('$d[A]/dt = - 2*(k_{on2}*[A]*[AB] - k_{off2}*[A_2B])$'))
display(Latex('$d[B]/dt = - (k_{on2}*[A]*[AB] - k_{off2}*[A_2B])$'))
display(Latex('$[A]+[AB]+2*[A_2B] = A_0$'))
display(Latex('$[B]+[AB]+[A_2B] = B_0$'))

print("As for the first QSSA, we can identify some relationships between the derivatives, and hence between the variables: d([A]+2*[A_2B])=0 and d([B]+[A_2B])=0, Hence,[A]+2*[A_2B] and [B]+[A_2B] are two constants in time. Let's call D the first one: [A]+2*[A_2B]=D, constant, and the second one will automatically stem from it:")
print("We have then: ")

display(Latex('$[A_2B] = (D - [A])/2$'))
display(Latex('$[AB] = A_0  -D$'))
display(Latex('$[B] = B_0 - [AB]-[A_2B]=B_0-A_0+D/2+[A]/2$'))

print("The fact that, in the QSSA approximation, we could identify relationships between the concentration implies that they are not independent anymore. The time derivatives, and thus the dynamics of both A_2B, A and B are governed by the same term: kon2*[A]*[AB] - koff2*[A_2B]. This was also true when using the first QSSA, and is a general statement.")
print("In other words, thanks to the relations above, the entire system reduces to just one ODE for [A] and once it's solved, all other variables might be obtained straightforwardly using the relations above. The ODE for [A] simplifies to:")
display(Latex('$ d[A]/dt = - 2*(k_{on2}*[A]*[AB] - k_{off2}*[A_2B]) = -2*(k_{on2}*[A]*(A_0  -D) - k_{off2}*((D - [A])/2))$'))

print("As for the first QSSA, this 1-variable ODE can be solved using the technique of the separation of variables [A] and t ... .")
print("Again here, the solution we will find depends on the constant D, which will be computed by equating the steady state values for A, B, AB and A_2B computed using the QSSA with those computed from the original, full ODE system.")


