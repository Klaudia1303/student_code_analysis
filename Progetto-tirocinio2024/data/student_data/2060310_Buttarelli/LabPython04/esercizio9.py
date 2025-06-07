n = int(input("Inserisci un numero maggiore di 0: "))
while n <= 0:
    n = int(input("Input non valido. Inserisci un numero maggiore di 0: "))
i = 1
n1 = 1
n2 = 1
somma = 1
while i <= n:
    if i == 1 or i == 2:
        print(1)
    else:
        somma = n1 + n2
        print(somma)
        n1 = n2
        n2 = somma
        
    i += 1
    
