n=0
while n<=0:
    n = int((input("Inserisci un numero intero maggiore di 0: ")))
i=1
while i<=n+1:
    if n%i==0:
        print(i)
    i=i+1
