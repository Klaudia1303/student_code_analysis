t=float(input('Inserire un valore che rappresenta una temperatura:' ))
c=input('Inserire un carattere tra F e C a rappresentare la scala utilizzata.' )
if c=='C' and t<=0:
    print('solida')
elif 1<t<99:
        print('liquida')
elif t>=100:
        print('gassosa')
elif c=='F':
    t1 = ((t-32)/1.8)
elif t1<=0:
    print('solida')
elif 1<t1<99:
    print('liquida')
elif t1>=100:
    print('gassosa')
