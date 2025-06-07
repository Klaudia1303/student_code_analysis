m=int(input('inserisci un intero che rappresenti un mese:'))
a=int(input('inserisci un intero che rappresenti un anno:'))
if m>12:
    print('input non valido')
elif m==12:
    print(str(1)+'/'+str(int(a+1)))
else:
    print(str(int((m+1)))+'/'+str(a))
