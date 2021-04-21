from IPython.display import display, Latex, Math

print("Equations 9-18 are space-dependent. 1-8 are regular ODEs. However, because the variables composing the ODEs might depend on space since they are coupled to 9-18, a partial time derivative is used. The equations 1-8 indicate the dynamics of either non-migrating cells (neurons, glial cells), large aggregate structures (amyloid-B, NFTs) which are thus also considered poorly mobile, and intracellular proteins (tau) for which I suppose the diffusion is considered so fast that a uniform equilibrium within cells is rapidly reached (sort of quasi steady state approximation). In contrast, equations 9-18 represent the dynamics of motile immune cells (macrophages, microglias), and of extracellular molecules/cytokines that are mobile, both of which are susceptible to spread in the entire brain tissue, which cannot be achieved instantaneously. Hence their space-dependent dynamics have to be fully accounted for. Among these, the Amyloid beta oligomer (soluble), Tumor Necrosis Factor alpha (Ta), Transforming Growth Factor beta (Tb), Interleukin 10 (I 10) and MCP-1 (P) are considered as freely diffusing, as illustrated by the pure diffusive term in the equations 9, 10, 15-18. All other species, including obviously the ones described by the non-space-dependent ODEs, but also the microglias and macrophages (Eqs 11,12 and 13,14 respectively) are not freely diffusing. ")
print("")
print("The left hand sides of equations 11, 12, 13, 14 are of the form:")

display(Latex('$\partial X / \partial t +\overrightarrow{nabla} \displaystyle \Bigg[ X*\overrightarrow{nabla(Y)} \Bigg],$'))

print("where X are migrating immune cells, microglias 1 and 2 in equations 11, 12 and macrophages 1 and 2 in equations 13, 14, and Y is in both cases a chemoattractant, HMGB-1 secreted by dead neurons for microglias and A0 the soluble amyloid-B for macrophages.")
print("")
print("We recognize in the form of these equations the form")
display(Latex('$\partial X / \partial t +\overrightarrow{nabla(J(X))},$'))
print("where J(X) can thus be interpreted as a flux of the quantity X.")
print("")
print("Therefore, the terms")
display(Latex('$ M_1*\overrightarrow{nabla(H)},$'))
print("and")
display(Latex('$ M_2*\overrightarrow{nabla(H)},$'))
print("simply represent a flux of M_1 and M_2 microglias along (and in the direction of) the gradient of HMGB-1, their chemoattractant, while")
display(Latex('$ \hat{M_1}*\overrightarrow{nabla(A_0)} ,$'))
print("and")
display(Latex('$ \hat{M_2}*\overrightarrow{nabla(A_0)},$'))
print("simply represent a flux of M_1 and M_2 macrophages along (and in the direction of) the gradient of A_0, their chemoattractant.")