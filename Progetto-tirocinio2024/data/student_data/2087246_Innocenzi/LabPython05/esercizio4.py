n1=int(input("Inserisci un numero intero: "))
n2=int(input("Inserisci un numero intero: "))
prodotto=0
for i in range(1, n2+1):
    prodotto=n1*i
    if(prodotto>=n2):
        break
    else:
        print(prodotto)