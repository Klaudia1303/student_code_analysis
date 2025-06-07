t=int(input('Inserire una temperatura: '))
if t>30:
    print('Molto caldo')
elif 20<t<=30:
    print('Caldo')
elif 10<t<=20:
    print('Gradevole')
else:
    print('Freddo')
