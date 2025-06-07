lato=int(input('Inserire il lato di un quadrato: '))

for i in range(lato):
    for j in range(lato):
        if i == 0 or i == lato-1 or j == 0 or j == lato-1 or j == i or j == lato-1-i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
