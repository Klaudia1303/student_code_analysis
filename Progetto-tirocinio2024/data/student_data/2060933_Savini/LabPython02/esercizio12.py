t= int(input('inserisci numero: '))
t1= input('inserisci F o C: ')
if t<=0 and t1=='C':
    print('solida')
if t>=100 and t1=='C':
    print('gassosa')
elif t>0 and t<100 and t1=='C':
    print('liquida')
if t<=32 and t1=='F':
    print('solida')
if t>=212 and t1=='F':
    print('gassosa')
elif t>32 and t<212 and t1=='F':
    print('liquida')
elif t1!= 'F' or t1!= 'C':
    print('input non valido')
