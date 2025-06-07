n=int(input('inserire un numeratore: '))
d=int(input('inserire un denominatore: '))


if n<d:
    print('propria')
elif n%d==0:
    print('apparente')
elif n%d!=0:
    print('impropria')

    

