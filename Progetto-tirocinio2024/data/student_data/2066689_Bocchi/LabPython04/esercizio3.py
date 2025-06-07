n=input('numero intero (* per terminare): ')
somma = 0

while n != '*':
    n= int(n)
    if n < 0:
        somma = somma + n
    n= input('numero intero (* per terminare): ')
print(somma)
