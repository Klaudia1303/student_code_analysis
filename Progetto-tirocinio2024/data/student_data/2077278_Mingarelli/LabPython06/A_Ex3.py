for i in range (1,9):
    for j in range (1,9):
        n=i*j
        d=n//8
        if n//8==8:
            print('100')
        else:
            print( d,n%8,sep='',end=' ')
    print(' ')
    
