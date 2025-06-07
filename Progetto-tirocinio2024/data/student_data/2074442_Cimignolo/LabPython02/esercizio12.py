a=float(input('inserisci temperatura: '))
b=input('inserisci scala: ')

if b=='C':
    if a<=0:
        print('solida')
    elif 0<a<100:
        print('liquida')
    else:
        print('gassosa')
elif b=='F':
    if a<=32:
        print('solida')
    elif a<32<212:
        print('liquida')
    else:
        print('gassosa')
else:
    print('carattere non valido')
