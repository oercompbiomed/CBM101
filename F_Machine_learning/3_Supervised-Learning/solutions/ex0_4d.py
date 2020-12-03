def tts(data, p=.75):
    N = data.shape[0]
    train_idxs, test_idxs = get_indeces(N, p)
    
    train_data = data[train_idxs]
    test_data = data[test_idxs]
    
    return train_data, test_data