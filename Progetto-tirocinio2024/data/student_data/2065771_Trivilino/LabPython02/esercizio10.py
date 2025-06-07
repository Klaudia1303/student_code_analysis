eta=float(input('Inserire l\'età del cane: '))
if 0<=eta<=2:
    print('La corrispondente età in età umana è:',eta*10.5)
elif eta>2:
    print ('La corrispondente età in età umana è:',(2*10.5)+((eta-2)*4))
else:
    print ('Inserire  un anno valido')
