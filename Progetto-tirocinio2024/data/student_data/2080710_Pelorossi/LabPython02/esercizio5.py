a=int(input('inserisci un anno:'))
if (a%4==0 and a%100!=0) or a%400==0:
    print('anno bisestile')
else:
    print('anno non bisestile')
