x=int(input('inserisci sequenza di numeri interi'))
somma=0
while x!=0:
    x=int(input('inserisci sequenza di numeri interi'))
    if x%3==0: 
        somma= somma+int(x)
print(somma)
