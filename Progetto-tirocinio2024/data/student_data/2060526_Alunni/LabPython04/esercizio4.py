n = int(input('inserisci una serie di numeri, la sequenza verrà interrotta quando sarà immesso il numero 0: '))
somma = 0
while not n==0 :
    if n%3==0 :
        somma = somma + n
    n = int(input('inserisci una serie di numeri, la sequenza verrà interrotta quando sarà immesso il numero 0: '))
print(somma)
