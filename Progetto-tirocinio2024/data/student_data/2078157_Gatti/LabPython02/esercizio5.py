#esercizio 5
a = int(input('inserisci un anno: '))
if a%100 != 0 and a%4 == 0:
    print('anno bisestile')
else:
    print('anno non bisestile')
