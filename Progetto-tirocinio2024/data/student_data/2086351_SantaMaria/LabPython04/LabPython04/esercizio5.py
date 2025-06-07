prodotto=1
n=int(input('Inserisci un intero: '))
i=0
while (n!=0 or n!=1) and i!=n:
    prodotto=prodotto*(n-i)
    i+=1
print(prodotto)
