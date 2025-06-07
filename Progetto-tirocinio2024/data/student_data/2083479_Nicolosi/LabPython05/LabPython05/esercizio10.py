l=int(input('Inserisci il lato (maggiore o uguale 2): '))
for i in range(l):
    for j in range(l):
        if i==0 or i==l-1:
            print('*',end='')
        elif j==0 or j==l-1:
            print('*',end='')
        elif j==i or j==l-1-i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
 