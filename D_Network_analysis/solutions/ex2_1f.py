
# same approach as in the previous notebook
degs = sorted(G.degree, key=lambda item:item[1], reverse=True)
degs[:5]