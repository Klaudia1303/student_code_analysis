i = 0
somma_N = 0
while i>=0:
    n = input('inserisci un numero: ')
    if n == '*':
        i=-1
    else:
        n = int(n)
        if n<0:
            somma_N += n
            i += 1
        else:
            i +=1
print(somma_N)
