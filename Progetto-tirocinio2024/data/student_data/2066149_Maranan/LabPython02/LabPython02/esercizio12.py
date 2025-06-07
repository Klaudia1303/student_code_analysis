t = int(input('Inserisci un valore per la temperatura dell\'acqua: '))
c = input('Inserisci uno tra C o F, per rappresentare la temperatura rispettivamente in\
 Celsius o in Fahrenheit: ')

if c == 'f':
    print('La temperatura inserita è in Fahrenheit')

    t = (t-32)/1.8
        
else:
    print('La temperatura inserita è in Celsius')

if t <= 0:
        print('Solida')

if t > 0 and t < 100:
        print('Liquida')

if t >= 100:
        print('Gassosa')


    
    
