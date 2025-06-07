#esercizio 11
a = int(input('inserisci il valore intero di una temperatura: '))
if a>30:
    print('molto caldo')
elif 20<a<=30:
    print('caldo')
elif 10<a<=20:
    print('gradevole')
else:
    print('freddo')
