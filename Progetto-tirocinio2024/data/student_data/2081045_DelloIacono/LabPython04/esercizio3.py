i=0
c=str(input('inserire un intero'))
while not(str(c)=='*'):
    if int(c)<0:
        i=i+1
    c=str(input('inserire un intero'))
    
print(i)
