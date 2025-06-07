#Elimina i valori x e y nell'intervallo [0,10]

x = int(input('intero x = '))
y = int(input('intero y = '))
n = 0

if x >= 0 and y >= 0 and x <= 10 and y <= 10:

    while n <= 10:
        if n != x and n != y:
            print(n)
            n = n+1
        else:
            n = n+1
        
else:
    print('input non valido')
