c=int(input('inserire un numero intero: '))
d=int(input('inserire un numero intero: '))
i=0
somma=0
if d>0:
    while (i<d):
        somma=somma+c
        i=i+1
else:
    while (i>d):
        somma=somma+c
        i=i-1
    somma=-somma
print(somma)
    
