n=int(input("Inserisci un numero: "))

if n%5!=0:
    while n%5!=0:
        n=int(input("Inserisci un numero: "))    
print(n//5)
