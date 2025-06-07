a=float(input('please type the \'a\' side: '))
b=float(input('please type the \'b\' side: '))
c=float(input('please type the \'c\' side: '))


if a>0 and b>0 and c>0:
    if a<b+a and b<c+a and c<b+a:
        if a==b==c:
            print ('equilatero')
        elif a==b:
            print ('isoscele')
        elif  a!=b and b!=c:
            print ('scaleno')


else:
    print ('input non valido.')
