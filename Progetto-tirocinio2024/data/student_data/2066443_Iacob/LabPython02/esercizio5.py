y = input('Insert year here: ')
y = int(y)
if y%4==0 and y%100!=0:
    print('Anno bisestile')
else: print('Anno non bisestile')
