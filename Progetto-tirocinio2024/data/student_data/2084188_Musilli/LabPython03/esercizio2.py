n=0
while n==0:
    n=int(input("Inserire un numero intero >0 per trovare tutti i suoi divisori: "))
    if n<1: print("Il numero inserito non è maggiore di 0.Reinserire il valore\n") 
i=1
while i<=n:
    if n%i==0: print("\n",i)
    i+=1
