from IPython.display import display, Latex
print("First, we expand the expression of the random variable of which we want to compute the expectation value:")
display(Latex('$ (N-<N>)^2 = N^2-2*N*<N>+<N>^2$'))
print("because <N> is just a number.")
print("")
print("Then we compute the expectation value of the sum of all terms as the sum of the expectation values of each term:")

display(Latex('$ <(N-<N>)^2> = <N^2>-<2*N*<N>>+<<N>^2>$'))
print("")
print("And finally we scrutinize all terms: the first one is the expectation value of the random variable N^2, which is what it is. 2*N*<N> is the product of a random variable, N, by a number, 2*<N>. Hence the expectation value of the product is the expectation value of the random variable times the number:")

display(Latex('$ <2*N*<N>> = 2*<N>*<N> = 2*<N>^2$'))
print("finally the last term is the expectation value of a number, that is not even a random variable. Hence its expectation value is itself!")
display(Latex('$ <<N>^2>=<N>^2$'))
print("")
print("Summing all three terms we get to simplify the second and the third to finally obtain:")

display(Latex('$ <(N-<N>)^2> = <N^2>-2*<N>^2+<N>^2 = <N^2>-<N>^2$'))
