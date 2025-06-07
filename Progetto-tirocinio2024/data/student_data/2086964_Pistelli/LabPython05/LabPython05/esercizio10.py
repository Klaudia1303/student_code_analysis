a=int(input('inserisci un numero '))
for i in range(a):
    for k in range(a):
        if i==0 or i==a-1:
            print('*',end='')
        elif k==0 or k==a-1:
            print('*',end='')
        elif k==i or k==a-1-i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
