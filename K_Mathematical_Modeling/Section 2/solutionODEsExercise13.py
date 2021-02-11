from IPython.display import display, Latex, Math

print("From the first conservation equation we get:")
display(Latex('$ [AB]=A_0-[A]-2*[A_2B]$'))

print("And from the second: ")
display(Latex('$ [B]=B_0-[A_2B]-[AB]=B_0-[A_2B]-(A_0-[A]-2*[A_2B]) = B_0-A_0+[A]+[A_2B]$'))

print("We reinject these expressions in the ODEs for dA/dt and dA_2B/dt, and the resulting equations depend only on A, A_2B and parameters:")



display(Latex('$ d[A_2B]/dt = k_{on2}*[A]*(A_0-[A]-2*[A_2B]) - k_{off2}*[A_2B]$'))
display(Latex('$ d[A]/dt = - k_{on1}*[A]*(B_0-A_0+[A]+[A_2B]) + k_{off1}*(A_0-[A]-2*[A_2B])- k_{on2}*[A]*(A_0-[A]-2*[A_2B]) + k_{off2}*[A_2B]$'))
