
#a)
bidx = iris.SepalWidth >= iris.SepalWidth.mean()
print(iris.loc[bidx,:])

#b)
iris.loc[bidx,:].shape[0]