s = input('Inserisci una stringa non vuota: ')

if (s != ''):
    if (s[:1] == s[-1:]):
        print('caratteri iniziale e finale uguali')
    else:
        print('caratteri iniziale e finale diversi')
