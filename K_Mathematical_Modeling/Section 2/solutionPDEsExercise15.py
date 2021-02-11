from IPython.display import display, Latex, Math

print("The density u(t,x,y) is the number of microtubules that have the total length between x and x+dx, and the GDP-domain length between y and y+dy. Hence, the situation is very similar to what it is for a number of cells of volume between V and V+dV, except that here the bin has two components, x and y")
print("For individual microtubules, we can express the rate of elongation due to polymerization of additional GTP-bound units, per unit time, as: ")
display(Latex('$a*[GTP],$'))
print("where [GTP] denotes the concentration in GTP-bound tubulin dimers.")
print("Similarly, the rate of shortening due to occasional unbinding of GTP-bound tubulin units from the (+) end is: ")
display(Latex('$b,$'))
print("And as a consequence the net increase of individual microtubule size during a small time increment dt is: ")
display(Latex('$(a*[GTP]-b).$'))
print("Similarly, the elongation rate of the GDP domain of individual microtubules due to hydrolysis is: ")
display(Latex('$\gamma.$'))

print("")

print("Those are rates for individual microtubules, but how does that affect the density? Using the exact same reasoning than for the cell size problem, we can write the number of microtubules that will leave the double bin x<Total length<x+dx,y<GDP length<y+dy (towards the next bin along x, i.e. x+dx<Total length<x+2*dx,y<GDP length<y+dy) because of the combined effects of polymerization-mediated elongation and of shortening, during a small time increment dt:")
display(Latex('$u(t,x,y)*(a*[GTP]-b)*dt/dx.$'))
print("And exactly like for the cell size distribution problem, there will be a similar (but not absolutely identical!) number of microtubules entering the bin from the bin at smaller length, i.e. the double bin x-dx<Total length<x,y<GDP length<y+dy:")
display(Latex('$u(t,x-dx,y)*(a*[GTP]-b)*dt/dx.$'))
print("Likewise, because of hydrolyzation that tends to elongate the GDP domain while leaving the total length unchanged, some microtubules will leave the double bin x<Total length<x+dx,y<GDP length<y+dy to enrich the bin with slightly longer GDP domain, i.e. the double bin x<Total length<x+dx,y+dy<GDP length<y+2*dy:")
display(Latex('$u(t,x,y)*\gamma*dt/dy,$'))
print("but at the same time, hydrolysis along microtubules with a slightly shorter GDP domain (i.e., the fraction \gamma*dt/dy of all microtubules in the double bin x<Total length<x+dx,y-dy<GDP length<y) will enrich the double bin x<Total length<x+dx,y<GDP length<y+dy on which we are writing the balance equation of:")
display(Latex('$u(t,x,y-dy)*\gamma*dt/dy,$'))
print("microtubules.")
print("")
print("Hence, putting all terms together, the difference between the density of microtubules with total length x and GDP length y between the times t+dt and t is:")

display(Latex('$u(t+dt,x,y)-u(t,x,y)=-u(t,x,y)*(a*[GTP]-b)*dt/dx+u(t,x-dx,y)*(a*[GTP]-b)*dt/dx - u(t,x,y)*\gamma*dt/dy +u(t,x,y-dy)*\gamma*dt/dy.$'))

print("Where we can divide by the time increment dt and recognize partial derivatives of u with respect to time, x and y: ")

display(Latex('$\partial u/\partial t=-(a*[GTP]-b)*(\partial u/\partial x) - \gamma*(\partial u/\partial y),$'))

print("which is nothing else thant Eq.1 in https://arxiv.org/abs/0811.2245.")