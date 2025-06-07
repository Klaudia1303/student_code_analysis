anno=input('Inserisci un anno: ')
if int(anno)%4==0 and int(anno)%100!=0 or int(anno)%400==0:
    print('anno bisestile')
else:
    print('anno non bisestile')
