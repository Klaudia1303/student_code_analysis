n = input('Insert number here: ')
n = int(n)
d = input('Insert number here: ')
d = int(d)
if n<d:
    print('Propria')
elif n%d==0:
    print('Apparente')
else: print ('Impropria')
