n=int(input("Inserisci un valore maggiore di 0: "))
i=0
j=1
ris=0
print(j)
while n>1:
    ris=i+j
    i=j
    j=ris
    n-=1
    print(ris)
