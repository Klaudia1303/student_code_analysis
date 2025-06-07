n = input('inserisci una serie di numeri, la sequenza verrà interrotta quando sarà immesso il carattere ‘*’: ')
p = 0
while not n=='*' :
    if (int(n))>0 :
        p = p + 1
    n = input('inserisci una serie di numeri, la sequenza verrà interrotta quando sarà immesso il carattere ‘*’: ')
print(p)
        
