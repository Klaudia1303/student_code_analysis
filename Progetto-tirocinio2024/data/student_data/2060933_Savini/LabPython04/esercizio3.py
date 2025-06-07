n= (input('inserisci un numero intero: '))
somma=0
while n!='*':
    if int(n)<0:
        somma=somma+int(n)
    n= input('inserisci un numero intero: ')
print(somma)
