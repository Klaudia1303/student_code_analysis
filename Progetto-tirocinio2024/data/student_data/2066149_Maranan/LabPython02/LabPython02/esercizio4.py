s = input('Inserisci una stringa:')
if len(s.strip()) !=0:
    if s[0] == s[-1]:
        print('caratteri iniziale e finale uguali')
    else:
        print('caratteri iniziale e finale diversi')

else:
    print('campo vuoto')
