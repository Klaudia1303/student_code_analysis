n=int(input('Inserire un numeratore:'))
d=int(input('Inserire un denominatore:'))
if d==0:
    print('Non è possibile dividere per',d)
else:
    if n<d:
        print('La frazione è propria')
    elif n%d==0:
        print('La frazione è apparente')
    elif n>d:print('La frazione è impropria')

