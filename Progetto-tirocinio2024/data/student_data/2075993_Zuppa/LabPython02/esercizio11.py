t=int(input('inserire una temperatura in celsius    '))
if t < -273 :
    print('non esiste temperatura più bassa dello zero assoluto')
else:
    if t>30:
        print('molto caldo')
    elif t>20:
        print('caldo')
    elif t>10:
        print('gradevole')
    else:
        print('freddo')
