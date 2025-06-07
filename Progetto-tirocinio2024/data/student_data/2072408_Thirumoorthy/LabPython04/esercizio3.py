n=input('inserisci sequenza di numeri interi')
somma=0
while n!='*':
    if int(n)<0:
        somma=somma+int(n)
        n=input('inserisci sequenza di numeri interi')
    else:
        n=input('inserisci sequenza di numeri interi')

print(somma)
   


      
