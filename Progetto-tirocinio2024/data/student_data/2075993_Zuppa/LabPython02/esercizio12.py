t=int(input('inserire la temperatura    '))
fc=input('inserire il tipo di scala    ')
if fc == 'F' or fc == 'C':
    if fc=='C':
        if t>=100:
            print('stato gassosa')
        elif t<=0:
            print('stato solida')
        else:
            print('stato liquida')
    if fc=='F':
        if (t-32)/1.8 >= 100 :
            print('stato gassoso')
        elif (t-32)/1.8 <= 0:
            print('stato solido')
        else:
            print('stato liquido')
else:
    print('errore input scala')
