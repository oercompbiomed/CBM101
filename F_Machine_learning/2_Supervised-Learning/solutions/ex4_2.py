idxs = df.isna().any(axis=1) # axis=1 does it row-wise
idxs