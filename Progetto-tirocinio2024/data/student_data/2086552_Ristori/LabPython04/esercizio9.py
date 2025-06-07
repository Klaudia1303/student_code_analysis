n=int(input("Inserire numero intero maggiore di zero:"))
primoNumero=int(1)
secondoNumero=int(1)
b=True
print(int(1),end="\n");print(1)
while b:
    sommaParziale=primoNumero+secondoNumero
    primoNumero=secondoNumero
    secondoNumero=sommaParziale
    print(sommaParziale)
    if sommaParziale>=n:
        b=False
    
