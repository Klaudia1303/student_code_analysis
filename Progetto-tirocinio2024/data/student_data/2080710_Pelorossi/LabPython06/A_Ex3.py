for i in range(0,10):
    for j in range(0,10):
        if i<8 and j<8:
            print(i,j,end='')
            print()
        elif i>=8 and j>=8:
            print(i+2,j+2,end='')
            print()
