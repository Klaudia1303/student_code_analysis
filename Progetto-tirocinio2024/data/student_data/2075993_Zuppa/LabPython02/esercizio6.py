n=int(input('inserire il numeratore   '))
d=int(input('inserire il denominatore   '))
if n<d:
    print('la frazione è propria')
elif n%d == 0 :
    print('la frazione è apparente')
else:
    print('la frazione è impropria')
