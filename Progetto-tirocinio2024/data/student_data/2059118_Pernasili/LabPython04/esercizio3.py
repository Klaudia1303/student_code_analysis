finito = False
i = 0

while not finito:
    n = input("Inserisci un numero intero (* per terminare): ")
    if n == '*':
        print(i)
        finito = True
    else:
        n = int(n)
        if n<0:
            i=i+n
        
        
