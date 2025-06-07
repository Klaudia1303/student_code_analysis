n=int(input("Inserisci un intero maggiore di 0: "))
while n<0:
    print("Numero non valido")
    n=int(input("Inserisci un intero maggiore di 0: "))
i=1
while i<=n/2:
    if n%i==0:
        print("\n",i)
    i +=1
print("\n",n)
