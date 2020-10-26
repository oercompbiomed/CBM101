n_nodes = G.number_of_nodes()
n_edges = G.number_of_edges()
n_possible_edges = n_nodes**2 - n_nodes #subtract the diagonal because self-connections are not allowed
print(n_edges/n_possible_edges)