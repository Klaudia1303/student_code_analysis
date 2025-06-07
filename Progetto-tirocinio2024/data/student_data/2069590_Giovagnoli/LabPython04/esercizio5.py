n=int(input("Inserire un numero intero maggiore o uguale a 0: "))
fattoriale=1
if n>=0:
    while n>0:
        fattoriale = fattoriale *n
        n-=1  
print("Il fattoriale di ",n," è: ",fattoriale)