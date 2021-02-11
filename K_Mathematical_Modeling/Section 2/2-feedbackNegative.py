import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
# we generate an empty graph
G = nx.DiGraph()
# we add 3 nodes with labels Input,A,B
G.add_nodes_from(["Input","A","B"]),
G.add_edge("Input","A")
G.add_edge("A","B",weight=1)
G.add_edge("B","A",weight=-1)

# we display the graph
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx(G,pos,node_size=1500, with_labels=True)
# compute the adjacency matrix of the network (and check it!)
A_matrix = nx.adjacency_matrix(G, nodelist=None)