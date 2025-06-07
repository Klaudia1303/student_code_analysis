t=float(input('Inserire valore temperatura: '))
m=input('Inserire un carattere tra F (Fahrenheit) e C (Celsius): ')
if(m=='F'):
    t1=(t-32)/1.8
    if(t1<=0):
        print('Solida')
    else:
        if(t1>=100):
            print('Gassosa')
        else:
            print('Liquida')
else:
    if(t<=0):
        print('Solida')
    else:
        if(t>=100):
            print('Gassosa')
        else:
            print('Liquida')

