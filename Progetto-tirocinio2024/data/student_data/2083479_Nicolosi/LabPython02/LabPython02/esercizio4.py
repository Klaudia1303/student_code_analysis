s=input('Inserisci una stringa non vuota: ')
if s[0]==s[len(s)-1:len(s)]:
    print('caratteri iniziale e finale uguali')
else:
    print('caratteri iniziale e finale diversi')