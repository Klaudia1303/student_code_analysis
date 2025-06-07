n=int(input('inserire numeratore: '))
d=int(input('inserire denominatore: '))
if n < d:
    print('la frazione n/d è propria')
elif n%d == 0:
    print(' la frazione n/d è apparente')
else:
    print('la frazione n/d è impropria')
