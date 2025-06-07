somma=0
continua=True
while continua==True:
    n=int(input("Inserisci un numero intero: "))
    if n==0:
        continua=False
        print(somma)
    if n%3==0:
        somma=n+somma
        
