x=int(input('inserisci valore anno: '))
if (x%4)==0 and x!=100 and (x%400)==0:
    print('anno bisestile')
else:
    (x%4)>1 and x==100 and (x%400)>1
    print('anno non bisestile')
