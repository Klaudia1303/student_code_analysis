finito = False
i = 0
while not finito:
    n =int(input("Inserisci un numero intero: "))
    if n == 0:
        print(i)
        finito = True
    else:
        n = int(n)
        i = n//3
        
        
