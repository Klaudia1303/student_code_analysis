n=input('numero intero: ')
somma = 0

while n != '*':
    n= int(n)
    if n > 0:
        somma = somma +1
    n= input('numero intero: ')
print(somma)
