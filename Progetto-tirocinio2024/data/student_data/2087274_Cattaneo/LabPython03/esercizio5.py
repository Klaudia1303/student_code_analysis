i=True
while i:
    x=input('stringa=')
    print(x[0]+x[-1])
    if x.isalpha() and x.islower():
        i=False
    
