n=input('inserire numero intero: ')
somma=0
while n!='*':
    a=int(n)
    if a<0:
        somma=somma+a
        n=input('inserire numero intero: ')
    else:
        n=input('inserire numero intero: ')
print(somma)
