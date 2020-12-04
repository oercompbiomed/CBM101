# mixing matrix
np.random.seed(42)
A = np.random.randn(4,3)

print(A.T)

# apply transformation
X = S @ A.T

# EXPLANATION:
# each column in A.T defines one of the linear combinations (4 in total)
# the rows define how much to add from each source. 
# E.g. the first combination will be (0.5*im1 - 0.14*im2 + 0.65*im3)