n=int(input('Numeratore: '))
d=int(input('Denominatore: '))
if n<d:
    print('La frazione è propria')
else:
    if n%d==0:
        print('La frazione è apparente')
    else:
        print('La frazione è impropria')
