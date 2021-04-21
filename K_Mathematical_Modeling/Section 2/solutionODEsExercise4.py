from IPython.display import display, Latex
display(Latex('$ d[AB]/dt = k_{on1}*[A]*[B] - k_{off1}*[AB]- k_{on2}*[A]*[AB] + k_{off2}*[A_2B]$'))
print("and")
display(Latex('$ d[A_2B]/dt = k_{on2}*[A]*[AB] - k_{off2}*[A_2B]$'))
print("and")
display(Latex('$ d[A]/dt = - k_{on1}*[A]*[B] + k_{off1}*[AB]- k_{on2}*[A]*[AB] + k_{off2}*[A_2B]$'))
print("and")
display(Latex('$ d[B]/dt = - k_{on1}*[A]*[B] + k_{off1}*[AB]$'))

print("Conservation equations:")
display(Latex('$ [A]+[AB]+2*[A_2B] = A_0$'))
print("and")
display(Latex('$ [B]+[AB]+[A_2B] = B_0$'))

print("or equivalently")
display(Latex('$ d[A]/dt+d[AB]/dt+2*d[A_2B]/dt = 0$'))
print("and")
display(Latex('$ d[B]/dt+d[AB]/dt+d[A_2B]/dt = 0$'))

print("Conclusion: the conservation equations are satisfied, regardless of the values of the time derivatives d[A]/dt, d[B]/dt, d[AB]/dt and d[A_2B]/dt.")
print("We note however than, in the particular case where these derivatives are 0, which will below be referred to as the steady state, we recover the expression of the dissociation constants of the two complexes: ")
display(Latex('$ K_{d1}= k_{off1}/k_{on1} = [A][B]/[AB]$'))
print("and")
display(Latex('$ K_{d2}= k_{off2}/k_{on2} = [A][AB]/[A_2B]$'))
print("both of which have the units of concentrations.")


