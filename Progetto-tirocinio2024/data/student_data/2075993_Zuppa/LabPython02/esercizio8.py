a=int(input('inserire un lato   '))
b=int(input('inserire un lato   '))
c=int(input('inserire un lato   '))
if a>0 and b>0 and c>0 :
    if a+b>c and a+c>b and b+c>a:
        if a==b and b==c:
            print('è un triangolo equilatero')
        elif a==b or a==c or b==c:
            print('è un triangolo isoscele')
        else:
            print('è un triangolo scaleno')
    else:
        print('input non valido')
else:
    print('input non valido')
