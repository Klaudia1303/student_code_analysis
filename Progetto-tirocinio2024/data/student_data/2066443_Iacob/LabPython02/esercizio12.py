t1 = input('Insert temperature here: ')
t1 = int(t1)
g1 = input('Insert "F" for Fahrenheit or "C" for Celsius: ')
if g1=='C':
    if t1<=0:
        print('Solida')
    elif t1>=100:
        print('Gassosa')
    else: print('Liquida')
elif g1=='F':
    if ((t1-32)/1.8)<=0:
        print('Solida')
    elif ((t1-32)/1.8)>=100:
        print('Gassosa')
    else: print('Liquida')
