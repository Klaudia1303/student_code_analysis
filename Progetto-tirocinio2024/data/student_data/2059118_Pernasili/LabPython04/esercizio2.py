finito = False
i = 0
while not finito:
    n=input("Inserisci un numero intero (* per terminare): ")   
    if n == '*':
        finito = True
        print(i)
    else:
        n =int(n)
        if n>0:
            i = i+1
            
