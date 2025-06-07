i = 0
j = 0
while i < 1:
    s = input('Inserisci un intero (* per terminare): ')
    if '*' in s:
        i = 1
    else:
        if '+' in s:
            s = int(s[1:])
        else:
            s = int(s)
        if s > 0:
            j += 1
print (j)
