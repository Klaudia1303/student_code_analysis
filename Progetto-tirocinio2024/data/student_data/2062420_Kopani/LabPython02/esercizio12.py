t=int(input('temperatura: '))
u=input('scegli "C" per usare i gradi Celsius oppure scegli "F" per usare i gradi Fahrenheit: ')
if u=='F':
    U=(t-32)/1.8
    if U<=0:
        print('solida')
    elif 0<U<100:
        print('liquida')
    elif U>=100:
        print('gassosa')
elif u=='C':
    if t<=0:
        print('solida')
    elif 0<t<100:
        print('liquida')
    elif t>=100:
        print('gassosa')
