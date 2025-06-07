anno = int(input('Inserisci un anno a tuo piacimento: '))

if anno%4==0 and anno%100!=0:
    print('anno bisestile')
else:
    print('anno non bisestile')
