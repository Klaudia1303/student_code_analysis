n=int(input("inserisci intero positivo maggiore di 1: "))
i=2
c=0
while i<=n:
    if n%i==0:
        i+=1
        c+=1
    else:
        i+=1
if c>1:
    print("numero non primo")
else:
    print("numero primo")
