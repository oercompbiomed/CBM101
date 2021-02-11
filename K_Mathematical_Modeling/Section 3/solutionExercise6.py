from IPython.display import display, Latex
print("We introduce the generating function (using the index names n,m,p instead of n_A,n_B,n_{AB} for conciseness): ")

display(Latex('$G(x,y,z,t)= \sum_{n,m,p=0}^{\infty} (x^n y^m z^p P_{n,m,p}(t)),$'))
print("")
print("where the probabilities P_{n,m,p}(t) satisfy the CME we have just derived (and rewritten with the simpler index names):")

display(Latex('$\partial P_{n,m,p}(t) /\partial t= k_{on}* \displaystyle \Bigg[(n+1)*(m+1)*P_{n+1,m+1,p-1}(t)-n*m*P_{n,m,p}(t) \Bigg]+k_{off}* \displaystyle \Bigg[(p+1)*P_{n-1,m-1,p+1}(t)-p*P_{n,m,p}(t) \Bigg]$'))



print("and we use the calculation rules for the sums over n,m,p to find the PDE for G:")

display(Latex('$\partial G /\partial t= k_{on}* (z-x*y)*\partial^2 G /\partial x \partial y+k_{off}* (x*y-z)*\partial G /\partial z$'))

print("")
print("which can be factorized to:")
display(Latex('$\partial G /\partial t= (z-x*y)* \displaystyle \Bigg[ k_{on}* \partial^2 G /\partial x \partial y-k_{off}*\partial G /\partial z \Bigg]$'))

print("To compute the expected values of the number of molecules A, B, and complexes AB, we remember that, from the definition of the one-variable generating function, we had:")

display(Latex('$<N>=d G /dx (x=1)$'))
print("When the generating function is a function of multiple variables, the idea is the same. We start from the definition of the expectation value:")

display(Latex('$<n_A>=\sum_{n,m,p}^{\infty} n*P_{n,m,p}(t)$'))
print("where we recognize an expression which is very similar than the expression of dG/dx, with the exception that the variables x, y, z don't seem to be there. This expression is exactly the expression we get we computing dG/dx at the particular point x=y=z=1:")
display(Latex('$<n_A>=\partial G /\partial x (x=1,y=1,z=1,t).$'))
print("Likewise,")

display(Latex('$<n_B>=\partial G /\partial y (x=1,y=1,z=1,t)$'))
display(Latex('$<n_{AB}>=\partial G /\partial z (x=1,y=1,z=1,t).$'))

print("")
print("To get ODEs for <n_A>, we have to differentiate <n_A> with respect to time, and assuming we can permute the derivation operations we get: ")

display(Latex('$\partial <n_A> \partial t=(\partial /\partial x) [\partial G/\partial t] |(x=1,y=1,z=1,t)$'))
display(Latex('$\partial <n_A> \partial t=(\partial /\partial x)\displaystyle \Bigg[ (z-x*y) *\displaystyle \Bigg(    k_{on}* \partial^2 G /\partial x \partial y-k_{off}*\partial G /\partial z                     \Bigg) \Bigg] (x=1,y=1,z=1,t)$'))
print("and similarly:")
display(Latex('$\partial <n_B> \partial t=(\partial /\partial y)\displaystyle \Bigg[ (z-x*y) *\displaystyle \Bigg(    k_{on}* \partial^2 G /\partial x \partial y-k_{off}*\partial G /\partial z                     \Bigg) \Bigg] (x=1,y=1,z=1,t)$'))
display(Latex('$\partial <n_{AB}> \partial t=(\partial /\partial z)\displaystyle \Bigg[ (z-x*y) *\displaystyle \Bigg(    k_{on}* \partial^2 G /\partial x \partial y-k_{off}*\partial G /\partial z                     \Bigg) \Bigg] (x=1,y=1,z=1,t)$'))
print("")
print("These equations can be simplified to:")

display(Latex('$\partial <n_A> \partial t=\displaystyle \Bigg[ -y *\displaystyle \Bigg(    k_{on}* \partial^2 G /\partial x \partial y-k_{off}*\partial G /\partial z                     \Bigg) +   (z-x*y) *\displaystyle \Bigg(    k_{on}* \partial^3 G /\partial x^2 \partial y-k_{off}*\partial^2 G /\partial z \partial x                     \Bigg)      \Bigg] (x=1,y=1,z=1,t)$'))
display(Latex('$\partial <n_B> \partial t=\displaystyle \Bigg[ -x *\displaystyle \Bigg(    k_{on}* \partial^2 G /\partial x \partial y-k_{off}*\partial G /\partial z                     \Bigg) +   (z-x*y) *\displaystyle \Bigg(    k_{on}* \partial^3 G /\partial x \partial y^2-k_{off}*\partial^2 G /\partial z \partial y                     \Bigg)      \Bigg] (x=1,y=1,z=1,t)$'))
display(Latex('$\partial <n_{AB}> \partial t=\displaystyle \Bigg[ \displaystyle \Bigg(    k_{on}* \partial^2 G /\partial x \partial y-k_{off}*\partial G /\partial z                     \Bigg) +   (z-x*y) *\displaystyle \Bigg(    k_{on}* \partial^3 G /\partial x \partial y \partial z-k_{off}*\partial^2 G /\partial z^2                     \Bigg)      \Bigg] (x=1,y=1,z=1,t)$'))

print("")
print("where, at the point x=y=z=1, the term (z-x*y) vanishes, and we finally get:")

display(Latex('$\partial <n_A> \partial t=\displaystyle \Bigg[ - \displaystyle \Bigg(    k_{on}* \partial^2 G /\partial x \partial y-k_{off}*\partial G /\partial z                     \Bigg)       \Bigg] (x=1,y=1,z=1,t)$'))
display(Latex('$\partial <n_B> \partial t=\displaystyle \Bigg[ - \displaystyle \Bigg(    k_{on}* \partial^2 G /\partial x \partial y-k_{off}*\partial G /\partial z                     \Bigg)       \Bigg] (x=1,y=1,z=1,t)$'))
display(Latex('$\partial <n_{AB}> \partial t=\displaystyle \Bigg[ \displaystyle \Bigg(    k_{on}* \partial^2 G /\partial x \partial y-k_{off}*\partial G /\partial z                     \Bigg)     \Bigg] (x=1,y=1,z=1,t)$'))

print("and we therefore recover the deterministic relations:")
display(Latex('$\partial <n_A> \partial t=\partial <n_B> \partial t = -\partial <n_{AB}> \partial t$'))
print("We note that this identity is not generally true in the stochastic limit, because we assume that the molecules are independent random variables. However, those relations hold true for the average numbers of molecules. In addition, we find that the stationary condition")
display(Latex('$\partial <n_A> \partial t=\partial <n_B> \partial t = \partial <n_{AB}>  \partial t = 0$'))
print("corresponds to the condition that ")
display(Latex('$\partial G \partial t=0$'))
print("for all values of x, y, and z. This is a way to implement the stationary condition in the formalism of the CME.")
print("The resolution of the corresponding PDE")
display(Latex('$\displaystyle \Bigg[ k_{on}* \partial^2 G /\partial x \partial y-k_{off}*\partial G /\partial z \Bigg] = 0$'))
print("should not be attempted assuming a separation of variables (G=f(x)*g(y)*h(z)) because this would correspond to an uncoupling of the values of n_A, n_B and n_AB in the joint probability distribution which is obviously not true. ")

