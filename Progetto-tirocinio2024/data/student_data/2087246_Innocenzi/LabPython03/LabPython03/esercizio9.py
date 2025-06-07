n=int(input("Inserisci un numero intero: "))
i=0
k=0

while(i<n):
    i=i+1
    if(n%i==0):
        k=k+1
        

if(k==2):
        print("Numero primo")
    
else:
    print("Numero non primo")
    