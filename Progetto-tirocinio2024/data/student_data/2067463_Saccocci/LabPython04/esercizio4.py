n=int(input('Inserire un intero("0" per terminare):'))
somma=0
while n!=0:
    if n%3==0:
        somma=somma+int(n)
    n=int(input('Inserire un intero("0" per terminare):'))
print(somma)
