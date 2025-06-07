t = int(input('Inserisci la temperatura: '))
if t > 30:
    print('molto caldo')
if t > 20 and t <= 30:
    print('caldo')
if t > 10 and t <= 20:
    print('gradevole')
if t <= 10:
    print('freddo')
