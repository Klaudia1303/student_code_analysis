t=int(input('temperatura'))
scala= input('C o F')
if scala=='C':
    if t<=0:
        print('solida')
    elif t>=100:
        print('gassosa')
    elif 0<t<100:
        print('liquida')
if scala=='F':
    C=(t-32)/1.8
    if C<=0:
        print('solida')
    elif C>=100:
        print('gassosa')
    elif 0<C<100:
        print('liquida')
