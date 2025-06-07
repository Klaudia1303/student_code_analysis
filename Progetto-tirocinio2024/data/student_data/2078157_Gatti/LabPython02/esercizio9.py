#esercizio 9
a = int(input('inserisci un numero intero da 1 a 12: '))
b = int(input('inserisci un anno: '))
if 1<=a<=12:
    if a==12:
        print(1,b)
    else:
        print(a+1,b)
else:
    print('input non valido')
