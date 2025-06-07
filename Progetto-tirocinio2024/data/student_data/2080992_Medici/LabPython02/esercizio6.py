n=input('Inserire il numeratore:')
n=int(n)
d=input('Inserire il denominatore :')
d=int(d)
if n<d:
    print('la frazione è propria')
elif n%d==0:
    print('la frazione è apparente')
else:
    print('la frazione è impropria')
