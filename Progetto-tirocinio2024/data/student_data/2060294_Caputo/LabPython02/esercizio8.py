a=input('inserisci un lato: ')
a=int(a)
b=input('inserisci un lato: ')
b=int(b)
c=input('inserisci un lato: ')
c=int(c)
if (a>0 and b>0 and c>0):
    if(a+b<=c):
        if(a+c<=b):
            if(b+c<=a):
                if(a==b==c):
                    print('è un triangolo equilatero')
                else:
                    if (a==b or a==c or c==b):
                        print('è un triangolo isoscele')
                    else:
                        print('è un triangolo scaleno')
            else:
                print('non è un triangolo')
        else:
            print('non è un triangolo')
    else:
        print('non è un triangolo')
else:
    print('hai inserito numeri negativi')

