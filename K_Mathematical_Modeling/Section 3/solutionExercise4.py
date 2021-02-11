from IPython.display import display, Latex
print("The elementary reactions change the number of mRNAs and proteins by one unit. If the system is expected to have, on average, dozens of mRNAs and even more proteins, fluctuations associated with individual reactions are small enough to use the FP approximation.")
print("However, the state of the promoter is a binary variable, hence we cannot use any kind of large number approximation on this stochastic variable, this would not make any sense. But since it's a binary variable, there are only two possible states, hence it is mathematically tractable to write one FP equation per state.")
print("So, as we did for the CME, we will write two coupled Fokker-Planck equations for the system with promoter off (0) and with promoter on (1). ")

print("")

print("Let's list the reactions R_mu that are accounted for in the CME:")
print("- activation of the promoter, with rate k_on")
print("- inactivation of the promoter, with rate k_off+n*k_inact")
print("- synthesis of a mRNA molecule, with rate nu_0*p, p being the state of the promoter p=1 if active, p=0 if inactive")
print("- synthesis of a protein, with rate nu_1*m, m being the number of mRNAs")
print("- degradation of mRNA molecules, with rate d_0 per unit molecule")
print("- degradation of proteins, with rate d_1 per unit molecule")
print("")
print("The first two of these reactions cannot be treated in the FP approximation. So, in the final hybrid equations, we won't modify them. The last 4 reactions, in contrast, give rise to terms of the type w(s+nu)*P(s+nu,t)-w(s)*P(s). Let's simplify these terms using the FP approximation.")
print("")
print("The FP approximation formula sums over the elementary reactions mu=1..M (M total number of reactions), and for each reaction we sum over the number N of stochastic variables. But because not all variables are modified by the reaction, for any reaction there is only a finite number of coefficients delta_mu,i which are different of 0, the ones that correspond to the molecular species i involved in the reaction. For synthesis/degradation reactions, only one coefficient will be different from 0, for conversion reactions that convert one species into another, 2 coefficients. For reactions that convert 2 species into a third one like the formation of a bimolecular complex, 3 coefficients will be different from 0, the ones with index i corresponding to the two interactors and to the complex. So, in general, these sums from i=1 to N in the general FP formula reduce to 1-2-3 terms. For the second order part, because there are two sums, we can have 4-9 terms. ")
print("Before summing over all reactions, let's have a look to each reaction independently. We'll start with the first Fokker-Planck-style term in the second CME: ")


display(Latex('$\nu_0* \displaystyle \Bigg( P_{m-1,n,1}(t)-P_{m,n,1}(t) \Bigg) $'))
print("")
print("The notation of the states and their probabilities with integer indexes m, n was well suited for a discrete formulation, like the CME. However, since the Fokker Planck approach is a continuous description of the system, we will use a function-like notation for the probabilities:")

display(Latex('$P_{m,n,1}(t) -------> P_{1}(m,n,t) $'))

display(Latex('$P_{m,n,0}(t) -------> P_{0}(m,n,t) $'))



print("")
print("and with this new notation the term above becomes:")
display(Latex('$\nu_0* \displaystyle \Bigg( P_{1}(m-1,n,t)-P_{1}(m,n,t) \Bigg) $'))
print("Let's now apply the FP approximation for this reaction. This reaction involves a transition from the state with m-1 mRNAs, n proteins and promoter is on (state s+delta_mu) to the state m mRNAs, n proteins and promoter is on (state s), which corresponds to a vector delta_mu (the difference between the two states) that has a component -1 only for the m-component; there is no change in n or promoter activity so the delta_mu,i with respect to these components of the state are 0.")
print("In addition, for this particular reaction the function w(s)*P(s,t) is simply:")
display(Latex('$w(s)*P(s,t) = \nu_0*P_{1}(m,n,t) $'))
print("(the rate function w is a constant, and the probability of the state s=m mRNAs, n proteins and promoter on is P_1(m,n,t) by definition).")
print("The first term of the FP approximation for this reaction will therefore be:")

display(Latex('$-1* \partial[\nu_0* P_{1}(m,n,t)]/\partial m = -\nu_0* \partial[P_{1}(m,n,t)]/\partial m $'))

print("")
print("To compute the second term of the FP equation, we have to sum over all the pairs of delta_mu,i * delta_mu,j that are not identically 0. If the reaction was involving 2 components, like for instance a molecule 1 converted in a molecule 2, the delta_mu vector that records the changes in state variables affected by the reaction would have 2 non trivial components, delta_mu,1 and delta_mu,2 (for a 1->2 conversion we would have delta_mu,1=+1 and delta_mu,2=-1), and thus there would be four terms: i=j=1, i=1 and j=2, i=2 and j=1 and i=j=2.")
print("But here, the mRNA synthesis reaction we are considering affect only m: so there is just one term that is not 0 in the double sum, the term with i=j=the index of the mRNA variable:")

display(Latex('$(-1)*(-1)* \partial^2[\nu_0* P_{1}(m,n,t)]/\partial m^2 = \nu_0* \partial^2[ P_{1}(m,n,t)]/\partial m^2 $'))
print("")
print("And thus in total, the FP approximation transforms the CME term ")
print("")
display(Latex('$\nu_0* \displaystyle \Bigg( P_{1}(m-1,n,t)-P_{1}(m,n,t) \Bigg) $'))
print("")
print("into the FP-like term:")
print("")
display(Latex('$ -\nu_0* \partial[P_{1}(m,n,t)]/\partial m + \nu_0* \partial^2[ P_{1}(m,n,t)]/\partial m^2 $'))


print("Likewise, the FP approximation transforms the CME terms ")
print("")
display(Latex('$\nu_1*m* \displaystyle \Bigg( P_{m,n-1,1}(t)-P_{m,n,1}(t) \Bigg)$'))
display(Latex('$\nu_1*m* \displaystyle \Bigg( P_{m,n-1,0}(t)-P_{m,n,0}(t) \Bigg)$'))
print("")
print("into the FP-like terms:")
print("")
display(Latex('$ -\nu_1*m* \partial[P_{1}(m,n,t)]/\partial n + \nu_1*m* \partial^2[ P_{1}(m,n,t)]/\partial n^2 $'))
display(Latex('$ -\nu_1*m* \partial[P_{0}(m,n,t)]/\partial n + \nu_1*m* \partial^2[ P_{0}(m,n,t)]/\partial n^2 ,$'))
print("")


print("the CME terms ")
print("")
display(Latex('$d_0* \displaystyle \Bigg( (m+1)*P_{m+1,n,1}(t)-m*P_{m,n,1}(t) \Bigg)$'))
display(Latex('$d_0* \displaystyle \Bigg( (m+1)*P_{m+1,n,0}(t)-m*P_{m,n,0}(t) \Bigg)$'))
print("")
print("into the FP-like terms:")
print("")
display(Latex('$ +d_0* \partial[m*P_{1}(m,n,t)]/\partial m + d_0* \partial^2[m*P_{1}(m,n,t)]/\partial m^2 $'))
display(Latex('$ +d_0* \partial[m*P_{0}(m,n,t)]/\partial m + d_0 *\partial^2[m*P_{0}(m,n,t)]/\partial m^2 ,$'))
print("")

print("and the CME terms ")
print("")
display(Latex('$d_1* \displaystyle \Bigg( (n+1)*P_{m,n+1,1}(t)-n*P_{m,n,1}(t) \Bigg)$'))
display(Latex('$d_1* \displaystyle \Bigg( (n+1)*P_{m,n+1,1}(t)-n*P_{m,n,1}(t) \Bigg)$'))
print("")
print("into the FP-like terms:")
print("")
display(Latex('$ +d_1* \partial[n*P_{1}(m,n,t)]/\partial n + d_1* \partial^2[n*P_{1}(m,n,t)]/\partial n^2 $'))
display(Latex('$ +d_1* \partial[n*P_{0}(m,n,t)]/\partial n + d_1* \partial^2[n*P_{0}(m,n,t)]/\partial n^2,$'))
print("")

print("When regrouping all the terms, the full model takes the form of coupled Hybrid Fokker-Planck/CME equations:")
print("")

display(Latex('$\partial P_{0}(m,n,t)/\partial t = (k_{off}+n*k_{inact} )* P_{1}(m,n,t)- k_{on} * P_{0}(m,n,t)-\nu_1*m* \partial[P_{0}(m,n,t)]/\partial n + \nu_1*m* \partial^2[ P_{0}(m,n,t)]/\partial n^2 + d_0* \partial[m*P_{0}(m,n,t)]/\partial m + d_0 *\partial^2[m*P_{0}(m,n,t)]/\partial m^2+ d_1* \partial[n*P_{0}(m,n,t)]/\partial n + d_1* \partial^2[n*P_{0}(m,n,t)]/\partial n^2$'))

print("")


display(Latex('$\partial P_{1}(m,n,t)/\partial t = - (k_{off}+n*k_{inact} ) * P_{1}(m,n,t)+ k_{on} * P_{0}(m,n,t)-\nu_0* \partial[P_{1}(m,n,t)]/\partial m + \nu_0* \partial^2[ P_{1}(m,n,t)]/\partial m^2-\nu_1*m* \partial[P_{1}(m,n,t)]/\partial n + \nu_1*m* \partial^2[ P_{1}(m,n,t)]/\partial n^2 + d_0* \partial[m*P_{1}(m,n,t)]/\partial m + d_0 *\partial^2[m*P_{1}(m,n,t)]/\partial m^2+ d_1* \partial[n*P_{1}(m,n,t)]/\partial n + d_1* \partial^2[n*P_{1}(m,n,t)]/\partial n^2$'))


print("")

print("Those hybrid equations are coupled PDEs for the functions P_0(m,n,t) and P_1(m,n,t): solving PDEs is within reach analytically! and even if not, it is less computationally expensive to perform numerically than a full simulation of the CMEs.")

