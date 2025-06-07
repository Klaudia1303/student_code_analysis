i = 0
somma = 0
while i == 0:
    a = input("inserisci un numero intero ('*' per terminare): ")
    a = int(a)
    if a == 0:
        i = i + 1
    elif a != 0:
        if a % 3 == 0:
            somma = somma + a
print(somma)
        
