a=int(input('inserisci un intero: '))
b=int(input('inserisci un altro intero: '))
c=int(input('inserisci un altro intero: '))
if (a>0 and b>0 and c>0 and a+b>c and b+c>a and a+c>b):
    if (a!=b and c!=b and a!=c):
        print ('scaleno')
    elif (a==b and a==c):
        print ('equilatero')
    else:
        print ('isoscele')
else:
    print ('input non valido')
