stop = False
while not stop:
    s = str(input('Insert string here: '))
    i = 0
    while i<len(s):
        x = s[i]
        i = i+1
    if ord(x)>100:
        print('Il primo carattere con codice Unicode maggiore di 100 è',x)
    else:
        print('Stringa consumata e carattere non trovato')
    stop = True
