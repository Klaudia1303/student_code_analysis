t= int(input('temperatura: '))
u= input('unita di misura: (F) o (C)')
u= u.upper()

if u== 'F' or u== 'C':
    if u== 'F':
        c=(t-32)/1.8
        if c<=0:
            print('solida')
        elif 0<c<100:
            print('liquida')
        elif c>=100:
            print('gassosa')
    else:
        if t<=0:
            print('solida')
        elif 0<t<100:
            print('liquida')
        elif t>=100:
            print('gassosa')
else:
    print('seleziona unita di misura corretta')
