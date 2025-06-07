n1 = int(input("inserisci un intero positivo: "))
n2 = int(input("inserisci un intero positivo: "))
multiplo = 1
while multiplo < n2:
    if n1*multiplo < n2:
        print(n1*multiplo)
    multiplo += 1
    
