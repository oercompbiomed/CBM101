
def mult(*args):
    p=1
    for num in args:
        p*=num
    return p
    
mult(1, 3, 5, 7)