t = int(input('inserisci un valore di temperatira: '+ )
s = input('temperatura in F o C? ')
if s=='C':
    if t<=0:
        print('solida')
    elif 0<t<100:
        print('liquida')
    else:
        print('gassosa')
if s=='F':
    C=(t-32)/1.8
    if C<=0:
        print('solida')
    elif 0<C<100:
        print('liquida')
    else:
        print('gassosa')
    





