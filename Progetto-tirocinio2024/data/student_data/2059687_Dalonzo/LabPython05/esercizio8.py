import math
lato = int(input('Inserire la base di un triangolo iscoscele (dispari e maggiore o uguale a 3) : '))

somma = 1
middle = int (lato / 2)
while(somma <= lato):
    print(' ' * middle + '*' * somma + ' ' * middle, end='\n')
    somma += 2
    middle -= 1
