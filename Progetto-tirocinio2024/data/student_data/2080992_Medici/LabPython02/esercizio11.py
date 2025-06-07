t=input('inserire la temperatura: ')
t=float(t)
if 30<t:
    print('molto caldo')
elif 20<t and t<=30:
    print('caldo')
elif 10<t and t<=20:
    print('gradevole')
else:
    print('freddo')

