from IPython.display import display, Latex
print("No, it is non-linear. It is clear when we expand the right hand side.")
print("It can be solved with a separation of variables. From the initial ODE, we can divide by P*(1-P/Pmax) and multiply by dt. This separates the variables, and we get:")
display(Latex('$ dP/(P*(1-P/Pmax)) = r*dt$'))
print("We can use the partial-fraction decomposition technique to express the complex fraction as a sum of two simple fractions:")
display(Latex('$ dP/(P*(1-P/Pmax)) =dP*(1/(P*(1-P/Pmax))) = - dP*Pmax*(1/(P*(P-Pmax))) = - dP*(1/(P-Pmax)-1/P)$'))


print("Then we integrate both sides of the equation, from the initial time t=0 to running time t:")
display(Latex('$ \int_{0}^{t} (d(-\ln (P-Pmax)+\ln (P) ))= \int_{0}^{t} (r) dt$'))

display(Latex('$ (-\ln (P(t)-Pmax)+\ln (P(t)) )- (-\ln (P(0)-Pmax)+\ln (P(0)) )= r*t$'))

print("And passing to the exponential:")
display(Latex('$ P(t)/(P(t)-Pmax)=P(0)/(P(0)-Pmax)* e^{r*t}$'))

print("A bit of algebraic manipulations give:")

display(Latex('$ P(t)=Pmax*P(0)*e^{r*t}] /(Pmax-P(0)+P(0)*e^{r*t}]$'))

print("where we eventually specify the initial population size P(t=0)=0.01*Pmax")
display(Latex('$ P(t)=Pmax *0.01*e^{r*t}] / [0.99+0.01*e^{r*t}]$'))

print("Once we know the solution P(t) at all times, it is easy to pick the population size at a given instant such as e.g. t=3/r or t=7/r: we just have to replace t by 3/r or 7/r in the above equation and we get:")
display(Latex('$P(t=3/r) = 0.17*Pmax $'))
display(Latex('$P(t=7/r) = 0.92*Pmax $'))


print("This entire derivation could be redone with a time dependent rate r(t), only the exponential e^{r*t} would become e^{\int_{0}^{t} r(t)dt}.")
print("However, if Pmax was a function of time then this derivation would not establish a correct separation of variables, and depending on how Pmax scale with t it could be either possible or not.")

print("You are now able to solve a logistic ODE. That's quite advanced mathematics. Congratulations! But hold on: more intesting stuff is coming... ")



