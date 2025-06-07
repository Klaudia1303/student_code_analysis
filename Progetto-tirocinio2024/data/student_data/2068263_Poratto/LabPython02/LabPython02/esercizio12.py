Tem=int(input('Inserisci Temperatura: '))
print('[F]=Fahrenheit [C]=Celsius')
Uni=input('Inserisci il carattere [C] o [F] in MAIUSCOLO: ')
if Uni=='C':
    if Tem<=0:
        print('solida')
    elif 0<Tem<100:
        print('liquida')
    elif Tem>=100:
        print('gassosa')
elif Uni=='F':
    if Tem<=32:
        print('solida')
    elif 32<Tem<212:
        print('liquida')
    elif Tem>=212:
        print('gassosa')



    

