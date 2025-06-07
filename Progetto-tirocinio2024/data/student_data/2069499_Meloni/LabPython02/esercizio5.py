anno=int(input('Inserisci anno da verificare '))
if(anno%4==0 and anno%100!=0 or anno%400==0):
    print('anno bisestile')
else:
    print('anno non bisestile')
