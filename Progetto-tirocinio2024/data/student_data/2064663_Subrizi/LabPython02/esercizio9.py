m = int(input('Inserisci il numero di un mese: '))
a = int(input('Inserisci un anno: '))

if m>=1 and m<12:
    print(m+1,a)
elif m==12:
    print(1,a+1)
else:
    print('input non valido')

