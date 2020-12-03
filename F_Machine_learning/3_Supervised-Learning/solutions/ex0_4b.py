def data_splitter(data, idxs):
    subsample = data[idxs]
    return subsample

## Note: matrices are indexed like mat[rows, cols]. If only one is provided, it is interpreted as mat[rows].