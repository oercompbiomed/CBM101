
# you could use .assign like above, but .apply will yield what you are looking for only
# and not the whole dataframe

ratio = iris.apply(lambda x : x.SepalWidth / x.SepalLength, axis=1)

print(ratio.mean(), ratio.std())
