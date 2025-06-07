i=int(1)
n=int(input("Inserisci un numero maggiore di 0: "))
while(n<=0):
    n=int(input("Inserisci un numero valido: "))
if(n>0):
    while(i<=n):
        if(n%i==0):
            print(i)
        i+=1
        
