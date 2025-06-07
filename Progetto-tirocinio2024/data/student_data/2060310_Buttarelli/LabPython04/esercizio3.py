n = str(input("Inserisci un numero intero (* per terminare): "))
somma = 0
while n != "*":
    n = str(input("Inserisci un numero intero (* per terminare): "))
    if n!= "*":
        n = int(n)
        if n < 0:
            somma += n
    n = str(n)
print("Somma numeri negativi:", somma)
