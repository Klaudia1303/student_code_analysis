n=int(input("Inserisci un numero intero:"))
i=n
if n==0 or n==1:
    print(1)
while(i!=1):
        n*=(i-1)
        i-=1 
print(n)
