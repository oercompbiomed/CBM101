def get_indeces(N, p):
    idxs = np.arange(N)
    n_train = int(N * p)
    train_idxs = idxs[:n_train]
    test_idxs = idxs[n_train:]
    
    return train_idxs, test_idxs