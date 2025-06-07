n = 0
somma = 0
finito = False
while not finito:
    n = int(input("inserisci un numero intero (0 per terminare): "))
    if n != 0 and n%3 == 0:
        somma += n
    if n == 0:
        finito = True
        print(somma)
