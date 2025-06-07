for i in range(9):
    for j in range(9):
        if i*j==64:
            print('100')
        elif i*j<8:
            z=i*j
            c=str(z)
            print('0'+c,end=' ')
        else:
            a=(i*j)//8
            b=str(a)
            x=(i*j)%8
            y=str(x)
            print(b+y,end=' ')
    if i!=8:
        print()
