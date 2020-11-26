
def ablate_test(G, neuron):
    G_abl = G.copy()
    G_abl.remove_node(neuron)
    H = linking_graph(G_abl, sensors, sinks, depth)
    flow_value,_ = nx.maximum_flow(H,'SOURCE','SINK')
    print(node, flow_value)