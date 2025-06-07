n1= input('inserisci numero: ')
n= int(n1)
d1= input('inserisci numero: ')
d= int(d1)
if n<d:
    print('propria')
elif n%d==0:
    print('apparente')
elif n%d!=0:
    print('impropria')
