from IPython.display import display, Latex
print("The are now 3 random variables, the number of mRNAs that can take all integer values m=0 to infinity, the number of proteins that can take all integer values n=0 to infinity, and the state of the promoter that can take only two values on and off, or 1 and 0.")
print("")
print("A state of the system is now characterized by a triplet of numbers (m,n,p) where m and n are integers and p=0 or 1 is the state of the promoter. All the transitions between states with m,n and m+-1,n+-1 accounted for in the previous model where the promoter is always on are still possible irrespective of the state of the promoter, with one exception though: the mRNA synthesis reaction (terms with rate nu_0) is not possible when the promoter is off. Those reactions do not change the state of the promoter: so they are transitions between states (m,n,p) and (m',n',p') only with p'=p. In addition, there are now elementary reactions that activate , and inactivate the promoter, with respective rates k_on and k_off. Those reactions involve the states (m,n,p) and (m'=m,n'=n,p') where p' is not equal to p.")
print("")
print("Because the random variable that describe the state of the promoter is binary, it is more convenient to write separately the CMEs for the p=0 state and the p=1 state.")
print("According to the statements above, the right hand side of the CME for P_{m,n,p=0} will include all terms from the previous model (which preserve the off state but modify m and n) with the exception of the mRNA transcription term (rate nu_0):")

display(Latex('$ \nu_1*m* \displaystyle \Bigg( P_{m,n-1,0}(t)-P_{m,n,0}(t) \Bigg) + d_0* \displaystyle \Bigg( (m+1)*P_{m+1,n,0}(t)-m*P_{m,n,0}(t) \Bigg)+ d_1* \displaystyle \Bigg( (n+1)*P_{m,n+1,0}(t)-n*P_{m,n,0}(t) \Bigg),$'))

print(" + the term corresponding to the inactivation of an already active promoter:")

display(Latex('$ k_{off} * P_{m,n,1}(t),$'))

print(" - the term corresponding to the activation of an inactive promoter:")

display(Latex('$ - k_{on} * P_{m,n,0}(t),$'))

print("leading to the final form for the CME:")

display(Latex('$ \partial P_{m,n,0}(t)/\partial t = k_{off} * P_{m,n,1}(t)- k_{on} * P_{m,n,0}(t)+\nu_1*m* \displaystyle \Bigg( P_{m,n-1,0}(t)-P_{m,n,0}(t) \Bigg) + d_0* \displaystyle \Bigg( (m+1)*P_{m+1,n,0}(t)-m*P_{m,n,0}(t) \Bigg)+ d_1* \displaystyle \Bigg( (n+1)*P_{m,n+1,0}(t)-n*P_{m,n,0}(t) \Bigg),$'))



print("Likewise, the CME for the states (m,n,p) where p=1 (active promoter) will include all terms from the previous model (which preserve the on state but modify m and n), minus the term corresponding to the inactivation of the active promoter and + the term corresponding to the promoter activation: ")


display(Latex('$ \partial P_{m,n,1}(t)/\partial t= - k_{off} * P_{m,n,1}(t)+ k_{on} * P_{m,n,0}(t)+ \nu_0* \displaystyle \Bigg( P_{m-1,n,1}(t)-P_{m,n,1}(t) \Bigg)+ \nu_1*m* \displaystyle \Bigg( P_{m,n-1,1}(t)-P_{m,n,1}(t) \Bigg) + d_0* \displaystyle \Bigg( (m+1)*P_{m+1,n,1}(t)-m*P_{m,n,1}(t) \Bigg)+ d_1* \displaystyle \Bigg( (n+1)*P_{m,n+1,1}(t)-n*P_{m,n,1}(t) \Bigg)$'))

print("It is noteworthy that in the particular cases where m=0 and n=0, the terms proportional to P_{m,n-1,p} and P_{m-1,n,p} with p=0 and 1 will disappear from the equations.")