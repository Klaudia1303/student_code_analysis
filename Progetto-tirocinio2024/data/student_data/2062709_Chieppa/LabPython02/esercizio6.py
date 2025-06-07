n=int(input('inserire numeratore: '))
d=int(input('inserire denominatore: '))
if n<d:
    print('propria')
elif n%d==0:
    print('apparente')
elif n>d and n%d!=0:
    print('impropria')
