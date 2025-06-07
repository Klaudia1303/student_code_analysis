n=int(input("Inserire un numero magiore o uguale a 0:"))
tot=1
if (n==1) or (n==0):
    print("Il fattoriale di n è =",1)
while n>1:
    tot*=n
    n-=1
print("Il fattoriale di n è =", tot)
    
        
