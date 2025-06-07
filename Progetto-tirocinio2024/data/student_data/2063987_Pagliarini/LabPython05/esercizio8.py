b=int(input('inserisci base triangolo dispari'))
d=1
if b%2!=0:
    m=(b-1)//2
    for i in range(m+1,0,-1):
        print(' '*(i-1),end='')
        print('*'*d,end='')
        print(' '*(i-1),end='')
        print()
        d+=2
else:
    print('deve essere dispari paglià')
