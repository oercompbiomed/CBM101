def invert(A):
    B = A.copy()
    B[B<0] *= -1
    return B