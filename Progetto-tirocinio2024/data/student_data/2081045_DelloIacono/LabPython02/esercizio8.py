a=int(input('inserire intero: '))
b=int(input('inserire intero: '))
c=int(input('inserire intero: '))
if (a<b+c and b<a+c and c<a+b) and (a>0 and b>0 and c>0):
    if a==b and c==a:
        print('equilatero')
    elif (a!=b and b!=c and c!=a):
        print ('scaleno')
    else:
        print('isoscele')
else:
    print('input non valido')
