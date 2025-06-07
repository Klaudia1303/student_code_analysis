b=True
while b:
    n1=int(input("Inserire un numero intero positivo: "))
    if n1<1:    print("\n\t\tValore immesso non valido (non è positivo)\n")
    else:   b=False
b=True
while b:
    n2=int(input("Inserire un numero intero positivo: "))
    if n2<1:    print("\n\t\tValore immesso non valido (non è positivo)\n")
    else:   b=False
print("\nLista multipli del primo numero più piccoli del secondo:")
for i in range(n1,n2):
    if i%n1==0: print("\n\t",i)
