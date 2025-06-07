finito=False
somma=0
while not finito:
    x=input('inserire stringa')
    somma=somma+1
    if x.find('a')!=-1 and x.find('c')!=-1:
        finito=True
print(somma)
