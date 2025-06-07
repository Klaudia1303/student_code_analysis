print('MANTIENI LA STESSA LUNGHEZZA \n')
var1 = input('Inserisci una stringa di testo: ')
var1 = str(var1)
var2 = input('Inserisci una stringa di testo: ')
var2 = str(var2)
var3 = 0
var3 = int(var3)

if len(var1) == len(var2):
    print('\nInput valido \n')
else:
    print('\nInput non valido')

while len(var1) == len(var2) and var3 != len(var1):
    print(var1[var3] + var2[var3], end='')
    var3 += 1


