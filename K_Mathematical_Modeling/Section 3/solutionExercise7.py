from IPython.display import display, Latex
print(" - the state s is characterized by the copy number of each species: s=(n_A, n_B,n_{AB})")
print(" - there are two reactions: the first one (mu=1) has rate w_1(s)= k_{on}*(n_A+1)*(n_B+1) and projects from the state s+delta_1=(n_A+1, n_B+1,n_{AB}-1) into the state s=(n_A, n_B,n_{AB}) which correspond to a state change vector delta_1=(1,1,-1); ")
print("and the reverse reaction (mu=2) with the rate w_2(s)= k_{off}*(n_{AB}+1) that projects from the state s+delta_2=(n_A-1, n_B-1,n_{AB}+1) into the state s, corresponding to a state change vector delta_2=(-1,-1,+1);")
print("With T denoting the Langevin mesoscopic integration time, the Langevin equations for the three variables n_A (i=1), n_B (i=2), and n_AB (i=3) are therefore:")


display(Latex('$n_A(t+T)-n_A(t) = (-1)*k_{on}*n_A(t)*n_B(t)*T  + (+1)*k_{off}*n_{AB}(t)*T + (-1)*\sqrt{k_{on}*n_A(t)*n_B(t)*T}*n_1 + (+1)*\sqrt{k_{off}*n_{AB}(t)*T}*n_2 $'))
display(Latex('$n_B(t+T)-n_A(t) = (-1)*k_{on}*n_A(t)*n_B(t)*T  + (+1)*k_{off}*n_{AB}(t)*T + (-1)*\sqrt{k_{on}*n_A(t)*n_B(t)*T}*n_1 + (+1)*\sqrt{k_{off}*n_{AB}(t)*T}*n_2 $'))
display(Latex('$n_{AB}(t+T)-n_A(t) = (+1)*k_{on}*n_A(t)*n_B(t)*T  + (-1)*k_{off}*n_{AB}(t)*T + (+1)*\sqrt{k_{on}*n_A(t)*n_B(t)*T}*n_1 + (-1)*\sqrt{k_{off}*n_{AB}(t)*T}*n_2 $'))


print("where n_1 and n_2 are two random numbers pulled from the normal distribution centered at 0 and of standard deviation 1, and that must be different at each time step (but are the same for all species since they represent the random number of reactions that happen between t and t+T).")






