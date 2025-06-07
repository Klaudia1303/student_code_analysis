for i in range(1,9):
    for j in range(1,9):
        k=i*j
        if i*j<8:
            print('0',k, end='\t')
        elif 8<=k<64:
            print(k//8,k%8, end='\t')
        else:
            print('100')
    print()
            
