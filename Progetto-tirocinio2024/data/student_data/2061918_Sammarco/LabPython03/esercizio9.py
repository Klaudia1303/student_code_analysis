n=int(input("inserisci un intero:"))
i=1
c=0
while i<=n:
    if n%i==0:
        c+=1
    i+=1
if c==2:
    print("l'intero è un numero primo")
else:
    print("l'intero non è un numero primo")
    
