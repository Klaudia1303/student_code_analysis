s=input('inerisci intero (*per terminare): ')
somma=0
while s!='*':
    s=input('inerisci intero (*per terminare): ')
    if s<0:
        somma=somma+1
print(somma)
