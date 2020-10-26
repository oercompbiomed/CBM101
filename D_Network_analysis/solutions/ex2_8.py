
btws = nx.betweenness_centrality(G)

sorted(btws.items(), key=lambda d:d[1], reverse=True) #you've seen this before

# Answer:
# IGF1 is the second most central in terms of betweenness
# also very visible from the histogram