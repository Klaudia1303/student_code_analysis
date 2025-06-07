n=int(input('please type the numerator: '))
d=int(input('please type the denominator: '))

if n<d:
    print('propria')
elif n%d==0:
    print('apparente')
elif n>d and n%d!=0:
    print('impropria')
