t=int(input('inserire temperatura: '))
gradi=input('inserire unità di misura: ')
if gradi=='C' and t<=0:
    print('solida')
elif gradi=='C' and 0<t<100:
    print('liquida')
elif gradi=='C' and 100<=t:
    print('gassosa')
if gradi=='F':
    t1=(t-32)/1.8
    if t1<=((0-32)/1.8):
        print('solida')
    if ((0-32)/1.8)<t1<((100-32)/1.8):
        print('liquida')
    if ((100-32)/1.8)<=t1:
        print('gassosa')
