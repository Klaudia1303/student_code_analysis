n=input("Inserire un numero inter (* per terminare): ")
somma=0
while n!='*':
    n=int(n)
    if n<0:
        somma=somma+n
    n=input("Inserire un numero inter (* per terminare): ")
print(somma)
