s=input('Inserire una stringa non vuota:')
if len(s)==0:
    print('La stringa inserita è vuota')
else:
    sf=s[-1]
    si=s[0]
    if sf==si:
        print('caratteri iniziale e finale uguali')
    else:print('caratteri iniziale e finale diversi')
