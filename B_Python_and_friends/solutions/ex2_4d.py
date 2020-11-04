for species in ['Iris-versicolor', 'Iris-setosa', 'Iris-virginica']:
    num = iris.loc[iris.Name == species].shape[0]
    
    print(species, ':', num)
    
# they are balanced