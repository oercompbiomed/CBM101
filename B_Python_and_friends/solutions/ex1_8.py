def duplicates(ls):
    if len(ls) != len(set(ls)): 
        print('It has duplicates')

def duplicates(ls):    
    for i, e in enumerate(ls):
        if e in ls[i+1:]: 
            print('It has duplicates')
            return
        

# there are many possible solutions...
