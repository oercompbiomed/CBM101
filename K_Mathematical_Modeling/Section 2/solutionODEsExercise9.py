from IPython.display import display, Latex
print("We use the QSSA to compute [SE(t)] as a function of [S(t)]:")
display(Latex('$ [SE(t)]= k_1*E_0*[S(t)]/(k_2+k_3+k_1*[S(t)])$'))
print("Let's make an important point here:")

display(Latex('$ [SE(t)]= [S(t)] * [k_1*E_0/(k_2+k_3+k_1*[S(t)])]$'))
print("In the (frequent) situation where the enzyme is in default compare to the initial substrate pool substrate, for most of the time evolution we have [S(t)]>>E0, and thus k1*[S(t)]>>k1*E_0 and then, obviously, k2+k3+k1*[S(t)]>>k1*E_0. Thus, the fraction in the equation above is always small, maybe with the exception of the very last minute of the reaction where there's almost no free substrate left. ")
print("And therefore, [SE(t)] is always much smaller than [S(t)].")

print("We next use the conservation of total substrate-like pool [S(t)]+[SE(t)]+[P(t)]=S_0 to compute [S(t)] as a function of [P(t)]. Thanks to the default enzyme approximation above, it's easy:")
display(Latex('$ [S(t)]=S_0 -[P(t)]$'))

print("from which we get [SE(t)] as a function of [P(t)]:")
display(Latex('$ [SE(t)]= (S_0 -[P(t)]) * k_1*E_0/(k_2+k_3+k_1*(S_0 -[P(t)]))$'))

print("And finally we can write the ODE for P(t):")
display(Latex('$ d[P]/dt = k_3*(S_0 -[P(t)]) * k_1*E_0/(k_2+k_3+k_1*(S_0 -[P(t)]))$'))

print("Now we need to solve it. First, we remark that using the variable [X(t)]=S_0 -[P(t)] would make things look nicer, on the right and side that is obvious, but also on the left hand side:")

display(Latex('$ d[P]/dt = dS_0/dt-d[X]/dt = 0-d[X]/dt = k_3*[X(t)] * k_1*E_0/(k_2+k_3+k_1*[X(t)])$'))
print("so")

display(Latex('$ d[X]/dt = - k_3*[X(t)] * k_1*E_0/(k_2+k_3+k_1*[X(t)])$'))

print("in which the X and time variables can be separated:")

display(Latex('$ d[X] * (k_2+k_3+k_1*[X])/[X] = - k_3* k_1*E_0*dt$'))

print("To prepare an equation for integration, it is convenient to write it as sum of terms that can be integrated separately:")

display(Latex('$ k_1*d[X]+(k_2+k_3)*d[X]/[X] = - k_3* k_1*E_0*dt$'))

print("And then we can integrate each term between the initial time t=0 where we put only substrate and enzyme in the test tube, and thus there is no product and thus X=S_0, and any time t where X=X(t):")

display(Latex('$ k_1*([X(t)]-S_0)+(k_2+k_3)*\ln ([X(t)]/S_0) = - k_3* k_1*E_0*t$'))

print("in which we can, if we want, put the product concentration [P(t)] back in place of [X(t)] using X(t)=S_0 -[P(t)]:")

display(Latex('$ - k_1*[P(t)]+(k_2+k_3)*\ln (1-[P(t)]/S_0) = - k_3* k_1*E_0*t$'))

print("This equation defines a relationship that implicitly links ´[P] to time and the model parameters. It is, therefore, a solution of the initial ODE problem. Going further and plot the function can be done with an easy computer program.")

print("So we might ask: why doing all this work, while eventually we'll still need a computer? First, often we can proceed until the end and write an explicit solution P(t)=... . And even when we can't like here, such a relationship can be analyzed in a more straightforward way than the initial ODE system, to find the asymptotics, infer how the different parameters affect the solution ... And also, computational solving of this final algebraic equation is much faster, robust and overall more reliable than solving the ODE system computationally from the beginning.")

