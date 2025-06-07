a=int(input('inserisci lato triangolo '))
b=int(input('inserisci lato triangolo '))
c=int(input('inserisci lato triangolo '))
if a>0 and b>0 and c>0 and a<(b+c) and b<(a+c) and c<(b+a):
    if a==b==c :
        print('triangolo equilatero')
    elif a!=b!=c :
        print('triangolo scaleno')
    elif a==b!=c or a==c!=b or b==c!=a :
        print('triangolo isoscele')
else : print('input non valido')
    
