n=int(input('Numeratore '))
d=int(input('Denominatore '))
if n<d:
    print('Frazione propria')
elif n>d and n%d!=0:
    print('Frazione impropria')
elif n%d==0:
    print('Frazione apparente')
