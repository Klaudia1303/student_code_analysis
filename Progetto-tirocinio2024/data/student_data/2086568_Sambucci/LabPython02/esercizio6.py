n=int(input('Inserire numeratore: '))
d=int(input('Inserire denominatore: '))
if(n<d):
    print('La frazione è propria')
else:
    r=n%d
    if(r>0):
        print('La frazione è impropria')
    else:
        print('La frazione è apparente')
