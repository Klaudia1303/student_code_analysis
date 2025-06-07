n=0
while n<3:
    n=int(input("Inserire un numero intero >2, \
per stampare tutti i numeri pari da 2 fino al numero inserito: "))
    if n<3: print("Il numero inserito non è maggiore di 2.\
Reinserire il valore\n") 
i=2
while i<n+1:
    if i%2==0:  print("\n",i)
    i+=2
