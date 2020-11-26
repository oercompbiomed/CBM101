
data.loc[:,'Neuron 1'].unique().shape # one way

data.describe(include='all').T.unique # another way
# should be 281