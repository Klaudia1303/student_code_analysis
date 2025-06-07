finito = False
while (not finito):
    s = input('Inserisci una stringa palindroma: ')
    nope = False
    k = 0
    while (k < (len(s) / 2)):
        if (s[k] != s[len(s) - 1 - k:len(s) - k]):
            nope = True
        k += 1
    if (not nope):
        print('Stringa palindroma di lunghezza: ' + str(len(s)))
        finito = True
        
