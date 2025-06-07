for i in range(1,9):
    for j in range(1,9):
        if i==8 and j==8:
           print(100)
        else:
            x=i*j
            ottale=str(x//8)+str(x%8)
            print(ottale,end='   ')
    print()
            
