n1=int(input("Inserisci primo intero positivo: "))
n2=int(input("Inserisci secondo intero positivo: "))
while n1<0 or n2<0:
    n1=int(input("Inserisci primo intero positivo: "))
    n2=int(input("Inserisci secondo intero positivo: "))
n=0
while n<n2:
    n +=n1
    if n<n2:
        print(n)
