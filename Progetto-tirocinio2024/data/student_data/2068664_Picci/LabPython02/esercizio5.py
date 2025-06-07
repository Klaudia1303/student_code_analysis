a = int(input('inserisci anno: '))
if a%4==0 and a%100!=0 or a%400==0:
    print('anno bisestile')
elif a%100!=0:
    print('anno non bisestile')
