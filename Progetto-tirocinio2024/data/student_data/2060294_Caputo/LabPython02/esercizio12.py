temp=input('iserisci una temperatura: ')
temp=float(temp)
grado=input('inserisci F se il grado è Fahrenheit \
oppure inserisci C se il grado è Celsius: ')
if (grado=='F'):
    temp=(temp-32)/1.8
    if (temp<=0):
        print('acqua solida')
    elif (0<temp<100):
        print('acqua liquida')
    elif (temp>=100):
        print('acqua gassosa')
    
else:
    if (temp<=0):
        print('acqua solida')
    elif (0<temp<100):
        print('acqua liquida')
    elif (temp>=100):
        print('acqua gassosa')
