a=int(input('inserisci un lato: '))
b=int(input('inserisci un lato: '))
c=int(input('inserisci un lato: '))
x=abs(a)
y=abs(b)
z=abs(c)
if int(x)==int(a) and int(y)==int(b) and int(z)==int(c) and int(a)<int(b)+int(c)and int(b)<int(a)+int(c) and int(c)<int(a)+int(b):
    if int(a)!=int(b) and int(b)!=int(c) and int(a)!=int(c):
        print('è un triangolo scaleno')
    elif int(a)==int(b) and int(a)==int(c) and int(b)==int(c):
        print('è un triangolo equilatero')
    elif (int(a)==int(b))!=int(c) or (int(b)==int(c))!=int(a) or (int(a)==int(c)!=int(b)):
        print('è un triangolo isoscele')
else:
    print('input non valido')

    
    
    
