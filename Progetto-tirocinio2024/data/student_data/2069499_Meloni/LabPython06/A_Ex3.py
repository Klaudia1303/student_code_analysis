for i in range(1,9):
    for j in range(1,9):
        if(i*j<8):
            print (i*j,' '*2, sep=' ',end=' ')
        else:
            dec=i*j
            resto=dec%8
            dec=dec//8
            if dec==8:
                dec=10
            print (dec,resto,' '*2, sep='', end=' ')
    print()
