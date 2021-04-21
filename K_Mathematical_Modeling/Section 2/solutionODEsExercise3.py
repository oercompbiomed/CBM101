from IPython.display import display, Latex
display(Latex('$ d[mRNA_{nuc}]/dt =  k_t - k_{exp} * [mRNA_{nuc}]$'))
print("and")
display(Latex('$ d[mRNA_{cyt}]/dt =  k_{exp} * [mRNA_{nuc}] - k_{deg} * [mRNA_{cyt}]$'))
print("No. This is because mRNAs are continuously produced (and degraded) at independent rates in the model, so there is no particular reason why their number should be conserved.")


