for i in range(1,9):
    for j in range(1,9):
        r10=i*j
        d=r10//8
        if i==8 and j==8:
            print(100)
            break
        print(d,r10%8,sep='',end=' ')
    print(' ')
        
    
