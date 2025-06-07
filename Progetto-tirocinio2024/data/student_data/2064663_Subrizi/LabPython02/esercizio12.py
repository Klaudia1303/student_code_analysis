t = float(input('Inserisci il valore della temperatura t = '))
carattere = input('Inserisci il carattere C per usare i Celsius, F per i Fahrenheit: ')

if carattere == 'C':
    if t<=0:
        print('solida')
    elif t>0 and t<100:
        print('liquida')
    else:
        print('gassosa')
elif carattere == 'F':
    t= (t-32)/1.8
    if t<=0:
        print('solida')
    elif t>0 and t<100:
            print('liquida')
    else:
        print('gassosa')
        
else:
    print('input non valido')
    
