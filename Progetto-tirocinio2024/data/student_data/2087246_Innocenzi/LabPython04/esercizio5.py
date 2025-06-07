n=int(input("Inserisci un numero: "))
i=1

while(n!=1):
    if(n==0):
        print(1)
    i*=n
    n-=1

print(i)
        
