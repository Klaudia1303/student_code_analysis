a=int(input('Inserire anno: '))
if(int(a/4)==a/4 and int(a/100)!=a/100 or int(a/400)==a/400):
    print('Anno bisestile')
else:
    print('Anno non bisestile')
