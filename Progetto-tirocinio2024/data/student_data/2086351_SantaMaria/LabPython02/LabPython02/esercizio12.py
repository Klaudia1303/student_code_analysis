t=float(input('Inserisci la temperatura: '))
T=(input('Inserisci un simbolo tra F e C: '))
if T=='C':
    if t<=0:
        print('solida')
    elif t>=100:
        print('gassosa')
    else:
        print('liquida')
elif T=='F':
    x=(t-32)/1.8
    if x<=0:
        print('solida')
    elif x>=100:
        print('gassosa')
    else:
        print('liquida')
else:
    print('input non valido')
