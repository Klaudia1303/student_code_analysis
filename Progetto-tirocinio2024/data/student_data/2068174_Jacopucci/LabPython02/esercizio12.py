temp=input('inserire il valore della teperatura: ')
temp=float(temp)
tip=input('inserire la tipologia di temperatura (C= Celsius, F= Fahrenheit): ')
if (tip=='F'):
    temp=(temp-32)/1.8
    if(temp<=0):
        print('solida')
    else:
        if (temp>=100):
            print('gassosa')
        else:
            print('liquida')
else:
    
    if(temp<=0):
        print('solida')
    else:
        if (temp>=100):
            print('gassosa')
        else:
            print('liquida')
