x=int(input('la dimensione del lato di un quadrato che sia un intero maggiore o uguale a 2: '))
for i in range(x):
    for j in range(x):
        if i==j or i+j==x-1 or i ==0 or j==0 or i==x-1 or j==x-1:
            print('*', end = '')
        else:
            print(' ', end='')
    print()
