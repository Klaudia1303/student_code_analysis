#Trova un carattere con codice Unicode maggiore o minore di 100

s = input('Scrivi una stringa = ')
n = 0
m = 1

a = s[n:m]

if s != '':
    while a <= 'd' and a != '' :
        n = n+1
        m = m+1
        a = s[n:m]

    if a <= 'd':
        print('stringa consumata e carattere non trovato')
    else:
        print('Il primo carattere con codice Unicode maggiore di 100 è',a)

