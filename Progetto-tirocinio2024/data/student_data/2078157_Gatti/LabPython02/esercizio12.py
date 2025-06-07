#esercizio 12
a = float(input('scegli il valore della temperatura dell\'acqua: '))
b = input('scegli la scala celsius "C" o fahrenheit "F": ')
if b=='C':
    if a<=0:
        print('solida')
    elif 0<a<100:
        print('liquida')
    else:
        print('gassosa')
else:
    c = float(a * 1.8 + 32)
    if c<=32:
        print('solida')
    elif 32<c<212:
        print('liquida')
    else:
        print('gassosa')
