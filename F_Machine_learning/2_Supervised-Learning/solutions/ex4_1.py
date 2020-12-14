np.any(df.isna().values)
# .values turns it into a numpy array, onto which you can apply np.any

#df.isna().any() can  also be useful
