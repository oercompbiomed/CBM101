
figsize = (18,13)
plt.figure(figsize=figsize)

pos = nx.kamada_kawai_layout(G)


nx.draw_networkx_nodes(G, pos, node_color=colors.values(),
                       node_size=node_degrees*10)

nx.draw_networkx_edges(G, pos, edge_color='gray')

nx.draw_networkx_labels(G, pos, font_size=9)

plt.show()