anno= int(input('Inserire un anno: '))
if anno%400==0:
    print('anno bisestile')
else:
    if anno%4==0 and anno%100!=0:
        print('anno bisestile')
    else:
        print('anno non bisestile')
