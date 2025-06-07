n=int(input('inserire numeratore'))
d=int(input('inserire denominare'))
if n<d:
    print('propria')
elif n>d and n%d==0:
    print('apparente')
else:
    print('impropria')
