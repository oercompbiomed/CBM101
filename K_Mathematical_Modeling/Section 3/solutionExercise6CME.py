from IPython.display import display, Latex
print("There are three random variables, the numbers of molecules A, B and AB (n_A, n_B, n_{AB}) that can in principle take any integer value if the pool is infinite. There are two microscopic reactions in this model, A+B--->AB with rate k_on*n_A*nB (if starting from a state with n_A molecules A and n_B molecules B),  and AB--->A+B with rate k_off*n_AB (if starting from a state with n_AB complexes). ")
print("The states of the system are defined by the triplets of integer numbers:")

display(Latex('$s=(n_A,n_B,n_{AB})$'))
print("Both types of elementary reactions can project the system into the state s=(n_A,n_B,n_{AB}), and away from it. The first reaction A+B--->AB creates one complex and removes one A and one B so to project in s=(n_A,n_B,n_{AB}) it has to start from s'=(n_A+1,n_B+1,n_{AB}-1). Thus, this corresponds to a term")

display(Latex('$+k_{on}*(n_A+1)*(n_B+1)*P_{n_A+1,n_B+1,n_{AB}-1}(t)$'))
print("")
print("and this same type of elementary reaction also projects the system away from the state s, corresponding to the corresponding negative term in the CME:")
display(Latex('$-k_{on}*(n_A)*(n_B)*P_{n_A,n_B,n_{AB}}(t)$'))
print("")
print("Likewise, the second reaction A´--->A+B removes one complex and releases one A and one B so to project in s=(n_A,n_B,n_{AB}) it has to start from s'=(n_A-1,n_B-1,n_{AB}+1). Thus, this corresponds to a term")

display(Latex('$+k_{off}*(n_{AB}+1)*P_{n_A-1,n_B-1,n_{AB}+1}(t)$'))
print("")
print("and this same type of elementary reaction also projects the system away from the state s, corresponding to the corresponding negative term in the CME:")
display(Latex('$-k_{off}*(n_{AB})*P_{n_A,n_B,n_{AB}}(t)$'))
print("")
print("The CME hence becomes:")
display(Latex('$\partial P_{n_A,n_B,n_{AB}}(t) /\partial t= k_{on}* \displaystyle \Bigg[(n_A+1)*(n_B+1)*P_{n_A+1,n_B+1,n_{AB}-1}(t)-n_A*n_B*P_{n_A,n_B,n_{AB}}(t) \Bigg]+k_{off}* \displaystyle \Bigg[(n_{AB}+1)*P_{n_A-1,n_B-1,n_{AB}+1}(t)-n_{AB}*P_{n_A,n_B,n_{AB}}(t) \Bigg]$'))
