#Calcola tutti i numeri pari compresi tra 2 e n

n = int(input('Scrivi un numero n > 2 = '))
c = 2

if n > 2:
    if n%2 == 0:
        while c != n+2:
            print(c)
            c = c+2
        
    elif n%2 != 0:
        while c != n+1:
            print(c)
            c = c+2
else:
    print('input non valido')





        
