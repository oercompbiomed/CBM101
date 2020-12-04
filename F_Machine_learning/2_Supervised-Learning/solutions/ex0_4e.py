# must also divide into X and y (features and labels)
def tts(data, p=.75):
 
    N = data.shape[0]
    train_idxs, test_idxs = get_indeces(N, p)  
    train = data[train_idxs]
    test = data[test_idxs]
   
    X_train, y_train = train[:, :-1], train[:, -1]
    X_test, y_test = test[:, :-1], test[:, -1]

    return X_train, X_test, y_train, y_test