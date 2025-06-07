n=input('inserisci una sequenza di numeri '0' per terminare: ')
somma=0
while not n=='*':
    if(int(n))<0 :
        somma=somma+int(n)
    n=input('inserisci una sequenza di numeri, '0' per terminare: ')
print(somma)
