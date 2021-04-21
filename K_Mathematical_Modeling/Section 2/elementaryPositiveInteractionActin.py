import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
# we generate an empty graph
G = nx.DiGraph()
# we add 2 nodes with labels Free actin, Filament length
G.add_nodes_from(["Free actin","Filament length"]),
G.add_edge("Free actin","Filament length")
# we display the graph
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx(G,pos,node_size=1500, with_labels=True)