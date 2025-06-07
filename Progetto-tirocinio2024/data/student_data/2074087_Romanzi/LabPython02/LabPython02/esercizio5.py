a=int(input('Anno '))
if a%4==0 and a%100!=0 or a%400==0:
    print('Anno bisestile')
else:
    print('Anno non bisestile')
