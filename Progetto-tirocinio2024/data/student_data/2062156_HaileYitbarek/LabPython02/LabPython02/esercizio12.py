t=float(input('inserire temperatura: '))
T=input('scegliere scala per la temperatura tra F e C: ')
C=(t-32)/1.8
if T==input(C):
    if t<=0:
        print('solida per t:',t,'°C')
    elif 0<t<100:
        print('liquida per t:',t,'°C')
    elif 100<=t:
        print('solida per t:',t,'°C')
else:
    if C<=0:
        print('solida per t:',t,'°C')
    elif 0<C<100:
        print('liquida per t:',t,'°C')
    elif 100<=C:
        print('solida per t:',t,'°C')
    
 
 
