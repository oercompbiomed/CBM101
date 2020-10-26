# Transforming the graph into an undirected graph
G = nx.Graph(G)

# shortest path
nx.shortest_path(G, 'EGF', 'GCG')