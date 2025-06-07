l = int(input('Lato di un quadrato (intero dispari maggiore o uguale a 3): '))


for i in range(l):
    for j in range(l):
        if (i==0) or (i==l-1) or (j==0) or (j==l-1): 
            print('*', end='')
        else:
            print(' ', end='')
    print()

