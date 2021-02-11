from IPython.display import display, Latex, Math

print("Nucleation, depolymerization and rescue are also affecting the lengths x and y, but they do act only on some very specific (x,y) bins.")
print("Nucleation, for instance, creates a certain density of very, very small microtubules (total length x almost 0) with no GDP domain (y=0). Hence, the nucleation process only affects the density u(t,0,0) and if nucleation happens with a rate proportional to GTP we have:")
display(Latex('$\partial u(t,0,0) / \partial t = k_{nuc}*[GTP].$'))
print("Likewise, depolymerization and rescue only affect a limited number of bins, those with x=y, so they only affect u(t,x,y=x). And because these events modify the total length x, they lead to a derivative with respect to x, but which must be taken along the DIRECTION y=x. That is not easy. So we need a better formulation.")
print("")

print("Another possibility is to mathematicall express the fact that there are in fact two types of microtubules: the microtubules with an existing GTP end, so x>y, to which the polymerization, shortening and hydrolysis dynamics we obtained in the previous exercise apply. Let's call u1(t,x,y) the density of these type 1 microtubules. In addition, we also have the microtubules which DO NOT have a GTP end, for which x=y. Let us call those type 2 microtubule, and denote u2(t,x) their density. u2 is a different function that u1, as it depends only on x since there is no need to distinguish the total length from the length of the GDP domain for type 2 microtubules, they are identical. Do the equations look better with those new definitions ?")

print("")

print("Then: by definition (see Figure above), depolymerisation affects only u2; on the other hand, the shortening of type 1 microtubules where x is almost equal to y (i.e., with a very very very small GTP domain) converts them into type 2 microtubules. Hence, the equation for type 2 microtubules will have a source term b*u1(0,x,y=x), where b is the rate of shortening of type 1 microtubules. Likewise, the rescue turns type 2 microtubules into type 1 microtubules, and if it happens with rate krescue this will generate a source term krescue*u2(t,x) in the equation for type 1 microtubules, and the opposite (degradation) term in the equation for u2. Hence, the equations can be written for u1 and u2: ")


display(Latex('$\partial u_1(t,x,y)/\partial t=-(a*[GTP]-b)*(\partial u_1/\partial x) - \gamma*(\partial u_1/\partial y)+k_{rescue}*u_2(t,x),$'))

display(Latex('$\partial u_2(t,x)/\partial t=-k_{depoly}*(\partial u_2/\partial x) -k_{rescue}*u_2(t,x)+b*u_1(t,x,x)$'))

display(Latex('$\partial u_1(t,0,0) / \partial t = k_{nuc}*[GTP]$'))

print("We can easily envision that this model is <b> ill-defined </b>: indeed, nothing prevents the nucleation of an infinite number of small microtubules, as can be seen by the constant, positive value of")
display(Latex('$\partial u(t,0,0) / \partial t$'))

print("")
print("Hence, we need to account for the fact that, when microtubule density increases, the pool of GTP is progressively consumed. This could be done, for instance, by adding an ODE system for the concentration of GTP-bound tubulin, [GTP], and GDP-bound tubulin, [GDP]. This would require to quantify how the different polymerization/nucleation and depolymerization/shortening events affect the concentrations [GTP] and [GDP]. We would first need to parametrize the number of tubulin dimers per unit length on the microtubule filaments, then to compute how many tubulin dimers (and of which type: GTP- vs GDP bound) are released to/consumed from the cytosol per unit time (looking at PDEs for du1/dt, du2/dt and du1(t,0,0)/dt). Then we would need to parametrize the total volume in which the concentrations [GTP], [GDP] are defined in order to convert these fluxes of GTP- and GDP-bound tubulin dimers to and from the filaments into changes in concentration. It would also require to define the rate of conversion of GDP-bound tubulin to GTP-bound tubulin in the cytosol. Doing this work and writing the corresponding balance equations will give ODEs for [GTP] and [GDP], which will be coupled to the PDEs for u1(t,x,y), u2(t,x) and u1(t,0,0). This is an interesting exercise, we encourage you to do it and send us your results. ")
