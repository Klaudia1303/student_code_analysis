for i in range(1,9):
    for j in range(1,9):
        d=i*j
        if i==8 and j==8:
            print(100)
            break
        print(d//8,d%8,sep='',end=' ')
    print(' ')
