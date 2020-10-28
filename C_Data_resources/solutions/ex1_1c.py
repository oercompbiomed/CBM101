
# by usingt he above trick we see that kidney_data.gsms is a dictionary (you can validate this)

type(kidney_data.gsms)

# a dict is a container of key,value pairs. The values in this case are of the class GEOparse.GEOTypes.GSM 
# e.g.
print(type(list(kidney_data.gsms.values())[0]))

## to get the available methods:
fst = list(kidney_data.gsms.values())[0]
dir(fst)

# for instance look at metadata:

fst.metadata