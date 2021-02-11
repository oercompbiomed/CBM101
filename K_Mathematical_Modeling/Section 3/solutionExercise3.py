from IPython.display import display, Latex
print("The promoter activity is still a random variable, more than even since it is now stochastically influenced both by its intrinsic rate of inactivation k_off, and by the protein-associated inactivation. Since in the state for which we write the CME there are n proteins, and each might inactivate the promoter with a rate k_inact, the total inactivation rate will be k_off+n*k_inact. Importantly, this additional molecular route does not directly affect the number of mRNAs or of proteins, so in terms of the system's states involved in the transition, those are exactly the same as for the intrinsic inactivation k_off. ")
print(" Hence, we can simply replace k_off by k_off+n*k_inact and the CMEs become:")

print("")

display(Latex('$ \partial P_{m,n,0}(t)/\partial t = (k_{off}+n*k_{inact}) * P_{m,n,1}(t)- k_{on} * P_{m,n,0}(t)+\nu_1*m* \displaystyle \Bigg( P_{m,n-1,0}(t)-P_{m,n,0}(t) \Bigg) + d_0* \displaystyle \Bigg( (m+1)*P_{m+1,n,0}(t)-m*P_{m,n,0}(t) \Bigg)+ d_1* \displaystyle \Bigg( (n+1)*P_{m,n+1,0}(t)-n*P_{m,n,0}(t) \Bigg),$'))

print("and")


display(Latex('$ \partial P_{m,n,1}(t)/\partial t= - (k_{off}+n*k_{inact}) * P_{m,n,1}(t)+ k_{on} * P_{m,n,0}(t)+ \nu_0* \displaystyle \Bigg( P_{m-1,n,1}(t)-P_{m,n,1}(t) \Bigg)+ \nu_1*m* \displaystyle \Bigg( P_{m,n-1,1}(t)-P_{m,n,1}(t) \Bigg) + d_0* \displaystyle \Bigg( (m+1)*P_{m+1,n,1}(t)-m*P_{m,n,1}(t) \Bigg)+ d_1* \displaystyle \Bigg( (n+1)*P_{m,n+1,1}(t)-n*P_{m,n,1}(t) \Bigg)$'))

