s=int(input("Inserisci un intero maggiore di 0: "))
prodotto=1
while s>0:
    if s==1:
        prodotto=prodotto*1
        print(prodotto)
    prodotto=s*prodotto
    s=s-1
    
