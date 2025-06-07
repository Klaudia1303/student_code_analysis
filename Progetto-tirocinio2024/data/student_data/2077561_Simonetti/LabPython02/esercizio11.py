temp=int(input('please type the current temperature in degrees (Celsius): '))
if temp>-273:
    if temp>30:
        print('molto caldo')
    elif temp>20 and temp<=30:
        print('caldo')
    elif temp>10 and temp<=20:
        print('gradevole')
    else:
        print('freddo')
else:
    print('impossible.')
