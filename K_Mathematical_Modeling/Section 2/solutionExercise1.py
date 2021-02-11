from IPython.display import display, Latex
display(Latex('$ dB_{inact}/dt = - k * A(t) * B_{inact}$'))
print("and")
display(Latex('$ dB_{act}/dt = k * A(t) * B_{inact}$'))
print("Because the derivative of the sum of two terms is the sum of the derivatives,")
display(Latex('$ d(B_{inact}+B_{act})/dt = dB_{inact}/dt + dB_{act}/dt = - k * A(t) * B_{inact} + k * A(t) * B_{inact} = 0.$'))
print("Hence, the total concentration of b does not change over time: it is a constant.")

