s=input('inserire un numero intero (0 per terminare): ')
somma=0

while s!='0':
    s=int(s)
    if s%3==0:
        somma=somma+int(s)
    s=input('inserire un numero intero (0 per terminare): ')
print(somma)
