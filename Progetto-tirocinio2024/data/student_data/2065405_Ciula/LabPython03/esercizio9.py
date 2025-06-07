n=int(input("Inserisci un numero: "))
i=2
p=bool(True)
while(i<n):
    if(n%i==0):
        p=False
    i+=1
if(p):
    print("Numero primo")
else:
    print("Numero non primo")
