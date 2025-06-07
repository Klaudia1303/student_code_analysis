n=int(input('Inserisci un numeratore: '))
d=int(input('Inserisci un denominatore: '))
if n<d:
    print('La frazione',n,'/',d,'è propria')
elif n%d==0:
    print('La frazione',n,'/',d,'è apparente')
elif n>d and n%d!=0:
    print('La frazione',n,'/',d,'è impropria')