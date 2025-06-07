n1=int(input("Inserisci un intero: "))
n2=int(input("Inserisci un intero: "))
i=0
prodotto=0
while i<n2:
    if n2==0 or n1==0:
        prodotto=0
    prodotto=prodotto+n1
    i+=1
print(prodotto)
