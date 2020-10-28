
# len(ligands) <--- you would expect this to work, but if you look at ligands.keys() you see the data is structured a little strangely

print(ligands.keys())

# the right way turns out to be:
len(ligands['ligandInfo']['ligand'])
