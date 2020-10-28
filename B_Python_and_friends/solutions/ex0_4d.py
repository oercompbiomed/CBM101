
def tts(data, p=.75):
    
    N = data.shape[0]
    train_idxs, test_idxs = get_indeces(N, p)
    
    train = data[train_idxs]
    test = data[test_idxs]
    
    return train, test
    
