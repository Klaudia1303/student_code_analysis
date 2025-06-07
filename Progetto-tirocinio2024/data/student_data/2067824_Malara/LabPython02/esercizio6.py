n=int(input('numeratore\t'))
d=int(input('deominatore\t'))
print(n,'/',d)
if n<d:
    print('propria')
elif n%d==0:
    print('apparente')
else:
    print('impropria')
