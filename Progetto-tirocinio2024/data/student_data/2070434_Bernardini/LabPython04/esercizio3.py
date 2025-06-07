x=0
somma=0
while x!='*':
    x=input('inserire numero')
    if x!='*':
        f=int(x)
        if f<0:
            somma=somma+f
print(somma)
