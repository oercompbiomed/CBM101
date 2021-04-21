import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
# we generate an empty graph
G = nx.DiGraph()
# we add 3 nodes with labels Input,1,2
G.add_nodes_from(["Input",1,2]),
G.add_edge("Input",1)
G.add_edge(1,2,weight=-1)
G.add_edge(2,1,weight=-1)


# we display the graph
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx(G,pos,node_size=1500, with_labels=True)
# compute the adjacency matrix of the network (and check it!)
A_matrix = nx.adjacency_matrix(G, nodelist=None)
# evolve the system overtime from these network interactions: 
# initial state: a=1, others are all 0
timemax = 10
delta_state = [0] * len(G)
initial_state = [1]
initial_state = initial_state + [0] * (len(G) - 1)
current_state = initial_state
aggregated_state = np.array(current_state)
time_step = 0.01
time = 0
while (time<timemax):
    time = time + time_step
    for i in range(0,len(G)):
        delta_state[i] = 0
        for k in range(0,len(G)):
            delta_state[i] = delta_state[i] + A_matrix[k,i] * current_state[k]
    for i in range(0,len(G)):
        current_state[i] = current_state[i] + delta_state[i] * time_step
    aggregated_state=np.c_[aggregated_state,current_state]
final_state = aggregated_state[:,-1]
# plot the time variations of all the node values
plt.figure()
plt.plot(aggregated_state[-1],'-')
plt.plot(aggregated_state[-2],'--')
plt.show()