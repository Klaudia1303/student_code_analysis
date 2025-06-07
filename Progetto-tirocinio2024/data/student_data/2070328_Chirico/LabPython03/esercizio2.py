#Calcola tutti i divisori di n

n = int(input('Scrivi un intero n>0 = '))
d = n

if n > 0:
    while d >= 1:
        if n%d == 0:
            print(int(n/d))
            d = d-1
        elif n%d != 0:
            d = d-1
else:
    print('input non valido')
