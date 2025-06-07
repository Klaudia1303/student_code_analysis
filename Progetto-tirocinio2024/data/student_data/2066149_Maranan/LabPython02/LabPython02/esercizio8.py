a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

if a>0 and b>0 and c>0:

    if a<b+c and b<a+c and c<a+b:

        if a!=b!=c:

            print('Il triangolo è scaleno')

        elif (a!=b and b==c) or (a==b and b!=c) or (a==c and b!=c):

            print('Il triangolo è isoscele')

        elif a==b and b==c:

            print('Il triangolo è equilatero')
                  
    else:
        print('input non valido')
    
else:
    print('input non valido')
