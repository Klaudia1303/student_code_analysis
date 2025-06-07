n=int(input("Inserisci un numero intero"))
somma=0
while n!=0:
    if n%3==0:
        somma+=n
    n=int(input("Inserisci un numero intero"))
print(somma)
