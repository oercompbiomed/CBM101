# one possible solution out of many:

numerical_cols = iris.describe(include=[np.number]).columns
iris.assign(total = lambda x : sum([x[feat] for feat in numerical_cols])).head().round(3)

# you could also just make a list of the column names by hand