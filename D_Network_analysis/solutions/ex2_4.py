nx.draw(G, node_size=1200, node_color='green', font_color='white',
    linewidths=0.25, font_size=10, font_weight='bold', with_labels=True, dpi=1000, pos=nx.circular_layout(G))
plt.title("circular")