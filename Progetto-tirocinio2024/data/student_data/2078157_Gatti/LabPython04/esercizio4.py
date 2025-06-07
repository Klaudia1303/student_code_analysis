n = int(input('inserisci un intero (0 per terminare): '))
somma = 0
while n != 0:
    if n % 3 == 0:
        somma = somma + n
    n = int(input('inserisci un intero (0 per terminare): '))
print(somma)
