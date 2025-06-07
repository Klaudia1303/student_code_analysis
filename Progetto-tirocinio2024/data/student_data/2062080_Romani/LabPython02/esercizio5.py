anno=int(input('Inserire anno: '))
if anno%4==0 and anno%100!=0 or anno%400==0:
         print('Anno bisestile')
else:
    print('Anno non bisestile')
