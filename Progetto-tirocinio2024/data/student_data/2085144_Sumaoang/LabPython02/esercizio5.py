anno = int(input('Inserire un anno:'))

if anno//4 and anno%4 == 0:
    print('anno bisestile')
else:
    print('anno non bisestile')
