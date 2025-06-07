n=-1
i=1
fattoriale=1
while n<0:
    n=int(input("Inserire un numero intero n: "))
if n==0 or n==1:
    print("Il fattoriale del numero inserito è 1")
else:
    for i in range(1, n+1):
        fattoriale = fattoriale * i
    print("Il fattoriale del numero inserito è "+str(fattoriale))
    
