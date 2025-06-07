i = 0
somma = 0
while i>=0:
    n = int(input('inserisci un numero: '))
    if n==0:
        i=-1
    else:
        if n%3==0:
            somma += n
            i += 1
        else:
            i+=1
print(somma)
