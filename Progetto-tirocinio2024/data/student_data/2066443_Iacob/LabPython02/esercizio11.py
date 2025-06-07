t = input('Insert temperature here: ')
t = int(t)
if 30<t:
    print('Molto caldo')
elif 20<t<=30:
    print('Caldo')
elif 10<t<=20:
    print('Gradevole')
elif t<=10:
    print('Freddo')
