m=int(input('insrisci il mese: '))
a=int(input("inserisci l'anno: "))
if 1<=m<12:
    print(m+1, a)
elif m==12:
    print(1, a+1)
else:
    print('input non valido')
