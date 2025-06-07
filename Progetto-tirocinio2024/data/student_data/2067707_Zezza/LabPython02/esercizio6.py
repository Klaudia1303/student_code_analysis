n=int(input('n: '))
d=int(input('d: '))
if n<d:
    print('propria')
elif n%d==0:
    print('apparente')
elif n>d and n%d!=0:
    print('impropria')
