
degs_srt = sorted(degs, key = lambda item : item[1], reverse=True)
print(degs_srt)

# explanation: it selects the second element, i.e. the degree, for each of the items
# If you are new to lambda functions, it is only syntactical convenience.
# we could have achieved the same using a regular function:

def func(item): return item[1]
sorted(degs, key = func, reverse=True)
