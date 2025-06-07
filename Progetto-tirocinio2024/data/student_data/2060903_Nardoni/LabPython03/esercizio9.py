n=int(input("Inserisci un numero intero"))
i=2
c=0
while i<=n/2 and c==0:
    if n%i==0:
        c+=1
    i+=1
if c==0:
    print("Numero primo")
else:
    print("Numero non primo")
