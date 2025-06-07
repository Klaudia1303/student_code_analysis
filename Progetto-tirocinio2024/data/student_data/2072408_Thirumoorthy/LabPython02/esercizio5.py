x= int(input('inserisci i dati di ingresso '))
if x%4==0 and x%100!=0 or x%400==0:
    print('anno bisestile')
else:
    print('anno non bisestile')
