s=input('inserire un numero intero (*per terminare): ')
c=0
somma=0

while s!='*':
    if int(s)<0:
        c+=1
        somma=somma+int(s)
    s=input('inserire un numero intero (*per terminare): ')
print('la somma dei numeri negativi=', somma)
