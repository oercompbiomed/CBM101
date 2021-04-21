from IPython.display import display, Latex, Math

print("Yes it is a linear system. In matrix form it can be written:")
display(Latex('$ dY/dt = A*Y+Y_0$'))

print("Where Y is the vector formed by the two unknown, time-dependent concentrations A(t) and B(t):")
display(Latex(' Y =  \\begin{bmatrix} A(t) \\end{bmatrix}  \n  \\begin{bmatrix} B(t) \\end{bmatrix} '))

print("Where Y_0 is the vector formed by the constants in the right hand side:")
display(Latex(' Y_0 =  \\begin{bmatrix} 1 \\end{bmatrix} \n \\begin{bmatrix} 0 \\end{bmatrix} '))

print("and the matrix A contains, on the first line, the coefficients of A(t) and B(t) in the right hand side of the first equation (in this order), and on the second line, the coefficients of A(t) and B(t) in the right hand side of the second equation:")
display(Latex(' A =  \\begin{bmatrix} 0 & -k_{B->A} \\end{bmatrix} \n \\begin{bmatrix} k_{A->B} &  0 \\end{bmatrix} '))

print("if the two rates are equal to k, the matrix simplifies to:")
display(Latex(' A = -k* \\begin{bmatrix} 0 & 1 \\end{bmatrix} \n \\begin{bmatrix} -1 & 0 \\end{bmatrix} '))

print("we can recognize the form of the matrix whose exponential has sin(t) and cos(t) terms (see formulas above), up to a multiplicative constant -k:")
display(Latex('´ A = -k* \\begin{bmatrix} 0 & 1 \\end{bmatrix} \n \\begin{bmatrix} -1 & 0 \\end{bmatrix} '))

print("So we know, because it is a linear system, that we can formally write the solution Y(t) as:")

display(Latex('$ Y(t)= e^{A*t} * (Y(t=0)+ A^{-1}*Y_0) - A^{-1}*Y_0 $'))

print("but thanks to the particular form of the matrix A, we know how to compute the exponential")


display(Latex(' e^{A*t} = \\begin{bmatrix} \cos(k*t) & -\sin(k*t)  \\end{bmatrix} \n \\begin{bmatrix} \sin(k*t) & \cos(k*t)   \\end{bmatrix} '))


print("and we can also remark that (or compute)")

display(Latex(' A^{-1} =1/k * \\begin{bmatrix} 0 & 1  \\end{bmatrix} \n \\begin{bmatrix} -1 & 0   \\end{bmatrix} '))


print("So that we can compute all terms in the solution. For instance,")

display(Latex(' A^{-1} * Y_0 = \\begin{bmatrix} 0  \\end{bmatrix} \n \\begin{bmatrix} -1/k   \\end{bmatrix} '))


print("The rest of the calculations will depend on the particular initial conditions, the vector Y(t=0). Let's assume that there is no A and no B at t=0, as in the simulations exercise 8, thus Y(t=0)=0. We can finish the matrix operations and we get the general solution (the 2 components of Y(t), in this order):")
display(Latex('$A(t)= \sin(k*t)/k $'))
display(Latex('$B(t)= -\cos(k*t)/k+1/k $'))

print("We obtain oscillatory functions of time. If kA->B was different from kB->A, the matrix A wouldn't have one of the particular forms with which the calculation of the exponential is straightforward. So we would have needed to diagonalize the matrix using a transformation P such that D=P^-1*A*P is diagonal, compute the exponential of the diagonal matrix, and invert the transformation to get exp(A). This procedure would have mixed the oscillatory functions, generating damped or amplified oscillations depending on the choice of parameters. A good exercise to do!")






