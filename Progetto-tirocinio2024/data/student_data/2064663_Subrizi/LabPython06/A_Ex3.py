for i in range(1,8):
    for j in range(1,8):
        prodotto=i*j
        if prodotto>=8:
            ris=' '
            while prodotto>0:
                resto=prodotto%8
                prodotto=prodotto//8
                ris=str(resto)+ris
            print(ris, end=' ')
        else:
            print('0'+str(prodotto), end=' ')
    print()
