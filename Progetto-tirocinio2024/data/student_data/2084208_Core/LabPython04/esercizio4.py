n='1'
somma=0
while int(n)!=0:
    if int(n)%3==0:
        somma=somma+int(n)
    n=input('Inserire un numero intero: ')
print(somma)
