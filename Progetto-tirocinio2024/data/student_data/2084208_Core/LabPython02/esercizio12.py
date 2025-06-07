x=int(input('Inserire una temperatura: '))
t=input('Inserire F per usare la scala Fahrenheit o C per usare Celsius: ')
if t=='C':
    if x<=0:
        print('solida')
    elif 0<x<100:
        print('liquida')
    elif x>=100:
        print('gassosa')
else:
    if ((x-32)/1.8)<=0:
        print('solida')
    elif 0<((x-32)/1.8)<100:
        print('liquida')
    elif ((x-32)/1.8)>=100:
        print('gassosa')
    
