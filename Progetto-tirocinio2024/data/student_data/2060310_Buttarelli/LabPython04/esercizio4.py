n = int(input("Inserisci un numero intero (0 per terminare): "))
somma = 0
while n != 0:
    n = int(input("Inserisci un numero intero (0 per terminare): "))
    if n % 3 == 0:
        somma += n
print("Somma numeri divisibili per 3:", somma)
