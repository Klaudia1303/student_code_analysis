an=int(input('inserire anno: '))
if (an%4==0 and not an%100==0 or an%400==0):
    print('anno bisestile')
else:
    print ('anno non bisestile')
