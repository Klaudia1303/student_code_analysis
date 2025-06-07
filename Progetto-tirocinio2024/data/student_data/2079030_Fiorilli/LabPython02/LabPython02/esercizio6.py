n=int(input('inserisci il numeratore: '))
d=int(input('inserisci il denominatore: '))
if n%d==0:
    print('apparente')
elif n<d:
    print('propria')
else:
    print ('impropria')
