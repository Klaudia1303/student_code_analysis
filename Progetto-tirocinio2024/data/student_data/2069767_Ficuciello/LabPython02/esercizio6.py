n=int(input('Inserire un numeratore:' ))
d=int(input('Inserire un denominatore:' ))
if n<d:
    print('propria')
elif n%d==0:
    print('apparente')
elif n>d and n%d!=0:
    print('impropria')
