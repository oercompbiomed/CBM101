
# utilize the fact that sets only have unique elements...
def duplicates(ls):
    if len(ls) != len(set(ls)): 
        print('It has duplicates')
    else: print('No duplicates')

        
# less elegant, but equally good
def duplicates(ls):    
    for i, e in enumerate(ls):
        if e in ls[i+1:]: 
            print('It has duplicates')
            return
    print('No duplicates')
        

# there are many possible solutions...