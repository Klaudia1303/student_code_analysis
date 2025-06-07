t=int(input('Inserisci temperatura '))
if t>30:
    print('Molto caldo')
elif 20<t<=30:
    print('Caldo')
elif 10<t<=20:
    print('Gradevole')
elif t<=10:
    print('Freddo')
