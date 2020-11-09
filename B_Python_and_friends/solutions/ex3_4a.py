def make_zero(A, k):
    B = A.copy()
    B[B < k] = 0
    return B