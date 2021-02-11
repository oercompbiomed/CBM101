print("The variable Pp/Ptot, i.e. the fraction of paused polymerases, seems to provide the best contrast between its minimal and maximal values as K_3 varies, regardless of the values of K_1 and K_2. In this example, it is not very surprising. Sometimes it is more difficult to find which model output is the most sensitive to a given parameter. ")
print(" The sensitivity is optimal for low values of K_3, i.e. K_3<K_1*K_2, where the slope of the curve Pp/Ptot=function(K_3) is the steepest.")
print(" To find out whether Pp/Ptot is sensitive to K_1 and or K_2, we need to give a value to K_3 and plot as a function of the other variables. ")
print("Starting with low K_3=0.3, we find that Pp is sensitive to K_2 mostly for K_2 lower than K_3, for larger values it becomes a flat curve. This remains true for larger K_3. And this is even more true for Pp/Ptot as a function of K_1, where the curve is flat for almost the entire range of K_1, regardless of the values of K_2 and K_3.")
print("")
print("So in summary, to measure differences across the genes in the pausing rate, we would need to 1) measure the fraction of paused polymerase complexes Pp/Ptot, and 2) try to work in experimental conditions where the other rates are as large as possible, where their influence on Pp/Ptot=function(K_3) is minimal. Maximizing K_1 could for instance be achieved by stabilizing the polymerase on DNA, which would reduce the k_off rate; maximizing K_2 could be achieved by selecting genes with low mRNA transcription rate, indicative in this model a low termination rate.")


