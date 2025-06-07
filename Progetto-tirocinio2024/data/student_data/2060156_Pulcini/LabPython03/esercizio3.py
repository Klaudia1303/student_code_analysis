finito=False
while not finito:
    n=int(input('inserisci intero:'))
    if n%5!=0:
        finito=False
    else:
        print(n//5)
        finito=True
        
    
