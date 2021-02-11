from IPython.display import display, Latex, Math

print("We denote u the microtubule density. Because we want to study the evolution of microtubules, time is obviously a relevant variable.")
print("Then, because all microtubules have potentially different lengths, we sort them into length bins, such as we did for size bins in a population of cells. Hence, we rather describe the density of microtubules which have a total length between x and x+dx, u(t,x).")
print("We are making progress. However, would such a u(t,x)-based model be sufficient to describe the hydrolysis of GTP into GDP along the microtubule, and hence the possibility of a GDP-bound (+) end which is at the origin of the microtubule catastrophe? Certainly not, because the density u(t,x) would not differentiate GTP-bound from GDP-bound tubulin units along the filament. Thus, we have to add a separate variable that represent the length of the GDP-bound tubulin domain (black on the figure): we will use a density u that depends on both the total length x, and the length of the GDP-bound domain y:")

display(Latex('$ u=u(t,x,y)$'))

print("Note that here, x and y are not space coordinates, just different variables.")
print("In such a model, how the polymerization, shortening, nucleation, depolymerization, hydrolysis, and rescue mechanisms can be parametrized naturally and easily. Indeed:")
print("From a state at time t where the density of microtubules of total length x and GDP-domain length y is u(t,x,y):")
print("")
print("- polymerization would tend to increase the density of longer microtubules (i.e. the u(t,X>x,y)), for instance at an elongation rate alpha*[GTP] (but we could use a [GTP]-independent rate in case of excess GTP...);")
print("")
print("- shortening would tend to do the opposite, i.e. increase the density of smaller microtubules (i.e. u(t,X<x,y)), for instance with a constant shortening rate beta;")
print("")
print("- nucleation would tend to increase the density of mitrotubules of small length x, adding GTP-bound tubulin only: so nucleation would only affect u(t,0,0);")
print("")
print("- depolymerization would increase the density of smaller microtubules, a bit like shortening, but would only affect microtubules without a GTP domain so microtubules with x=y; hence, depolymerization will only affect u(t,x,y=x);")
print("")
print("- similarly, rescue would increase the density of larger microtubules, a bit like polymerization, but would only affect microtubules without a GTP domain, so only affect u(t,x,y=x);")
print("")
print("- hydrolysis won't affect the length component of the density of microtubules: rather, hydrolysis will increase the density of microtubules with the same length and a longer GDP domain, so u(t,x,Y>y), for instance with a constant rate gamma of GDP-domain elongation.")

