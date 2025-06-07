t=int(input('Temperatura '))
if t>30:
    print('Molto caldo')
elif t<=30 and t>20:
    print('Caldo')
elif t<=20 and t>10:
    print('Gradevole')
else:
    print('Freddo')
