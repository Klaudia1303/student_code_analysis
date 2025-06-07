n=int(input("Inserire un numero intero >= 0: "))
fattoriale=1
while n!=0:
    fattoriale=fattoriale*n
    n-=1
print(fattoriale)
