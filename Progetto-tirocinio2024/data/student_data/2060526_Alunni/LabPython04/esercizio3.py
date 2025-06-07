n = input('inserisci una serie di numeri interi, la sequenza verrà interrotta quando sarà immesso il carattere ‘*’: ')
somma = 0
while not n=='*' :
    if (int(n))<0 :
        somma = somma + int(n)
    n = input('inserisci una serie di numeri interi, la sequenza verrà interrotta quando sarà immesso il carattere ‘*’: ')
print(somma)
