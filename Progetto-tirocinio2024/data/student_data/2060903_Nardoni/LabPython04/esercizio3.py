n=input("Inserisci un numero intero")
somma=0
while n!="*":
    n=int(n)
    if n<0:
        somma+=n
    n=input("Inserisci un numero intero")
print(somma)
