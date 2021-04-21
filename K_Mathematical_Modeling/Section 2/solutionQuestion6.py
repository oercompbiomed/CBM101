print("Now there are 3 steady states: (prey=0, predators=0); (prey=5, predators=0); and(prey=2, predators=2). The first 2 are unstable however, they don't have the same kind of unstability: while, from (0,0), a tiny increase in preys is amplified but not immediately followed by and increase in predators, from (5,0) a tiny increase in preys leads to a decrease in preys (looks like stability), but accompanied by a simultaneous increase in predators. So, while the (0,0) instability is along the prey axis, the (5,0) instability has a predator axis component. The third steady state (2,2) is stable, as all surrounding arrows converge to it. ")
print("When starting from (preys=4, predators=2.5), following the arrows we converge straight to the stable steady state).")
print("When starting from (preys=0, predators=4), following the arrows we first observe a drop in predator population due to the total absence of preys until we get close to the (0,0) state, then followed by an increase in preys with barely no increase in predator population until preys reach the limit population the environment can sustain (preys=pmax=5), from which the system eventually escape and converge to the stable state.")
print("Thus, the phase portrait allows to guess the dynamical trajectory that the system will follow depending on the initial conditions. In the presence of multiple stable states or limit cycles in the phase portrait, it allows to predict which final state the system will reach depending on the initial conditions, and possibly how we can transit between stable states. Despite this information is mostly qualitative, with the exception of the steady states and limit cycles which are quantitatively obtained, it is of outmost importance to understand the behavior of dynamical systems for which we cannot access the full time-dependent solution.")