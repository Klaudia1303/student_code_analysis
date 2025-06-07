t = int(input('inserisci temperatura: '))
fc = input('inserisci F o C: ')
if fc=='C':
    if t<=0:
        print('solida')
if fc=='C':
    if t>=100:
        print('gassosa')
if fc=='C':
    if t>0 and t<100:
        print('liquida')
if fc=='F':
    if (t-32)/(1.8)<=0:
        print('solida')
if fc=='F':
    if (t-32)/(1.8)>=100:
        print('gassosa')
if fc=='F':
    if (t-32)/(1.8)>0 and (t-32)/(1.8)<100:
        print('liquida')
        
