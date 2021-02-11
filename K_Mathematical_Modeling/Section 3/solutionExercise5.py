from IPython.display import display, Latex
print("If the promoter is always on, we have only two stochastic variables, the numbers of mRNAs and proteins, and both can take all integer values from 0 to infinity in principle. So this situation is ideal to use the formalism of the generating function.  Because we have two stochastic variables, we will use the 2-variables generating function:")

display(Latex('$G(x,y,t)= \sum_{n,m=0}^{\infty} (x^m y^n * P_{m,n}(t)) $'))

print("where x is associated with the index m and thus is associated with mRNAs, and y is associated with m, proteins.")

print("To find the PDE satisfied by G, we multiply the CME by x^m*y^n and sum over all possible values of m and n:")

display(Latex('$\sum_{m,n}^{\infty}x^m*y^n*\partial P_{m,n}(t)/\partial t=\sum_{m,n}^{\infty} x^m*y^n* \displaystyle \Bigg[ \nu_0* \displaystyle \Bigg( P_{m-1,n}(t)-P_{m,n}(t) \Bigg)+ \nu_1*m* \displaystyle \Bigg( P_{m,n-1}(t)-P_{m,n}(t) \Bigg) + d_0* \displaystyle \Bigg( (m+1)*P_{m+1,n}(t)-m*P_{m,n}(t) \Bigg)+ d_1* \displaystyle \Bigg( (n+1)*P_{m,n+1}(t)-n*P_{m,n}(t) \Bigg) \Bigg],$'))

print("The left hand side is the time derivative of the generating function:")



display(Latex('$\sum_{m,n}^{\infty}x^m*y^n*\partial P_{m,n}(t)/\partial t=\partial /\partial t \displaystyle \Bigg[ \sum_{m,n}^{\infty}x^m*y^n*P_{m,n}(t) \Bigg] = \partial G /\partial t$'))

print("and all the terms from the right hand side can be computed following the calculation rules that we have just demonstrated in the notebook:")




display(Latex('$\sum_{m,n}^{\infty} x^m*y^n* P_{m-1,n}(t)=x*G(x,y,t)$'))
display(Latex('$\sum_{m,n}^{\infty} x^m*y^n* P_{m,n}(t)=G(x,y,t)$'))
display(Latex('$\sum_{m,n}^{\infty} x^m*y^n* m*P_{m,n-1}(t)=x*y*\partial / \partial x G(x,y,t)$'))
display(Latex('$\sum_{m,n}^{\infty} x^m*y^n* m*P_{m,n}(t)=x*\partial / \partial x G(x,y,t)$'))
display(Latex('$\sum_{m,n}^{\infty} x^m*y^n* (m+1)*P_{m+1,n}(t)=\partial / \partial x G(x,y,t)$'))
display(Latex('$\sum_{m,n}^{\infty} x^m*y^n* m*P_{m,n}(t)=x*\partial / \partial x G(x,y,t)$'))
display(Latex('$\sum_{m,n}^{\infty} x^m*y^n* (n+1)*P_{m,n+1}(t)=\partial / \partial y G(x,y,t)$'))
display(Latex('$\sum_{m,n}^{\infty} x^m*y^n* n*P_{m,n}(t)=y*\partial / \partial y G(x,y,t)$'))

print("")
print("Bringing all terms together, we obtain the PDE for G(x,y,t):")

display(Latex('$ \partial G /\partial t = \nu_0*(x-1)*G+\nu_1*x*(y-1)*\partial G/ \partial x +d_0*(1-x)*\partial G/ \partial x+d_1*(1-y)*\partial G/ \partial y$'))


print("")
print("If the promoter state is not automatically on, it is also a stochastic variable. However, it does not take all integer values, it is only a binary variable, so there is no point including it in the generating function as a third variable. So, similar to the approach we used for Fokker Plank equations, we will define two generating functions that differ only in that one will use the coefficients P_{m,n,0}(t) and the other P_{m,n,1}(t), i.e. respectively the joint probabilities in the off and on states: ")

display(Latex('$G_0(x,y,t)= \sum_{n,m=0}^{\infty} (x^m y^n * P_{m,n,0}) $'))

display(Latex('$G_1(x,y,t)= \sum_{n,m=0}^{\infty} (x^m y^n * P_{m,n,1}) $'))

print("")
print("Following exactly the same derivation, we obtain for the case where there is no negative feedback of protein levels on the promoter activation:")

display(Latex('$ \partial G_0 /\partial t = k_{off}*G_1-k_{on}*G_0+\nu_1*x*(y-1)*\partial G_0/ \partial x +d_0*(1-x)*\partial G_0/ \partial x+d_1*(1-y)*\partial G_0/ \partial y$'))
display(Latex('$ \partial G_1 /\partial t = - k_{off}*G_1+ k_{on}*G_0+\nu_0*(x-1)*G_1+\nu_1*x*(y-1)*\partial G_1/ \partial x +d_0*(1-x)*\partial G_1/ \partial x+d_1*(1-y)*\partial G_1/ \partial y$'))

print("and in the case where there is a negative feedback and thus the number of proteins n affects the off rate which becomes k_off+k_inact*n, we obtain: ")

display(Latex('$ \partial G_0 /\partial t = k_{off}*G_1+k_{inact}*y*\partial G_1 /\partial y-k_{on}*G_0+\nu_1*x*(y-1)*\partial G_0/ \partial x +d_0*(1-x)*\partial G_0/ \partial x+d_1*(1-y)*\partial G_0/ \partial y$'))
display(Latex('$ \partial G_1 /\partial t = - k_{off}*G_1-k_{inact}*y*\partial G_1 /\partial y+ k_{on}*G_0+\nu_0*(x-1)*G_1+\nu_1*x*(y-1)*\partial G_1/ \partial x +d_0*(1-x)*\partial G_1/ \partial x+d_1*(1-y)*\partial G_1/ \partial y$'))
