a=int(input('inserire lunghezza lato: '))
b=int(input('inserire lunghezza lato: '))
c=int(input('inserire lunghezza lato: '))


if (a>0 and b>0 and c>0):
    if a==b and c!=a:
        print('isoscele')

if (a>0 and b>0 and c>0):
    if (a!=c and c!=b and a!=b): 
            print('scaleno')

if (a==b and a==c):
    print('equilatero')
