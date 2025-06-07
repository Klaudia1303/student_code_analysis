anno=int(input('Inserisci un anno '))
x=anno%4
y=anno%100
z=anno%400
if (x==0 and y!=0) or z==0:
    print('Anno bisestile')
else:
    print('Anno non bisestile')
