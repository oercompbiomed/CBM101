print(distance_matrix.shape)

# ANSWER:
#Instead of the expected 2D array (matrix), the distances are stored in a condensed
# 1D array because distances are redundant (we get 2 for each pair).
#How indexing works is dealt with behind the scenes.

# the full matrix would have shape (100, 100). 
#(100**2 - 100)/2