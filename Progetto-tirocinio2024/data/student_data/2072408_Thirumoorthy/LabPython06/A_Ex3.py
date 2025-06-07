for i in range (1,9):
    for j in range (1,9):
        r=i*j
        tb=r//8
        if i==8 and j==8:
            print(100)
            break
        print(tb,r%8, sep='',end=' ')
    print('')
