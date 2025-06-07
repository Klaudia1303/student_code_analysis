s = input('Inserisci una stringa: ')

n = 0
finito = False
while (not finito and n < len(s)):
    print (s[n])
    if (ord(s[n]) > 100):
        finito = True
        print('Il primo carattere con codice Unicode maggiore di 100 è ' + s[n])
    elif (n == len(s) - 1):
        finito = True
        print('Stringa consumata e carattere non trovato')
    n += 1
