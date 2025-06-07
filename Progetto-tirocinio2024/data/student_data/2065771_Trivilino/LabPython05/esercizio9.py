lato=int(input('Inserire il lato di un quadrato dispari: '))
spazio=' '*(lato-2)
print('*'*lato)
for i in range(1,lato-1):
    print(('*'+spazio+'*'))
print('*'*lato)
