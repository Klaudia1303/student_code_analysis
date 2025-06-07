temp=int(input('Inserire temperatura: '))
if temp<=10:
    print('freddo')
elif temp>10 and temp<=20:
    print('gradevole')
elif temp>20 and temp<=30:
    print('caldo')
elif temp>30:
    print('molto caldo')
