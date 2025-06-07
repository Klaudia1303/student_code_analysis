anno=int(input('inserire anno: '))

if (anno%4==0 and anno%400==0):
         print('anno bisestile')
else:
    if anno%100==1:
        print('anno non bisestile')
