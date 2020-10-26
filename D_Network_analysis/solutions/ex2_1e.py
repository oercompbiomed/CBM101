
# we use the same function from 1_network_graphs_students
def extract_subgraph(G, node):
    new_G = nx.Graph()
    for neighbor in G.neighbors(node):
        new_G.add_edge(node, neighbor)
    return new_G

# then plot
akt1_G = extract_subgraph(G, 'AKT1')
nx.draw(akt1_G, with_labels=True)
plt.show()


# alternatively you could display the edges between AKT1's neighbors too
nx.draw(G.subgraph(akt1_G.nodes), with_labels=True)