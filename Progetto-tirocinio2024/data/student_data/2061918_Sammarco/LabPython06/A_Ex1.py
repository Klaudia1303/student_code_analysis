n1=int(input("inserisci un intero positivo:"))
n2=int(input("inserisci un secindi intero positivo:"))
s=2
for i in range(s,n1+1):
    if n2%i!=0:
        if n1%i==0:
            print(i)

        
        
