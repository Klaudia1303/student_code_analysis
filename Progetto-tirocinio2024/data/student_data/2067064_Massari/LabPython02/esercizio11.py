temp= int(input('inserire una temperatura: '))
if temp>30:
    print('molto caldo')
elif 20<temp<=30:
    print('caldo')
elif 10<temp<=20:
    print('gradevole')
elif temp<=10:
    print('freddo')
