s = int(input("inserisci numeri interi per stampare la somma dei numeri \
divisibili per 3. ('0' per terminare): "))
somma = 0
while s != 0:
    if s % 3 == 0:
        somma += s
    s = int(input("inserisci numeri interi per stampare la somma dei numeri \
    divisibili per 3. ('0' per terminare): "))
print(somma)
