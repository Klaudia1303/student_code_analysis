lato = int(input('Inserire il lato del quadrato dispari e maggiore o uguale a 3 : '))

for i in range(0, lato):
    if(i == 0 or i == lato - 1):
        print('*' * lato)
    else:
        print('*' + ' ' * (lato - 2) + '*')

