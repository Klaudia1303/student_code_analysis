n=int(input('inserire valore numeratore: '))
d=int(input('inserire valore denominatore: '))

x=n/d

if d>n:
    print('propria')
if d==n*2:
    print('apparente')
if n>d:
    print('impropria')


