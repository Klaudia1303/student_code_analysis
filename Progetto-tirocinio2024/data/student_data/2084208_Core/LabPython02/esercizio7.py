n1=int(input('Inserire un numero intero: '))
n2=int(input('Inserire un secondo numero intero: '))
n3=int(input('Inserire un terzo numero intero: '))
if n1>n2:
    if n2>n3:
        print('',str(n1),'\n',str(n2),'\n',str(n3))
    elif n2<n3:
        if n3>n1:
            print('',str(n3),'\n',str(n1),'\n',str(n2))
        else:
            print('',str(n1),'\n',str(n3),'\n',str(n2))
else: 
    if n1>n3:
        print('',str(n2),'\n',str(n1),'\n',str(n3))
    else:
        if n3>n2:
            print('',str(n3),'\n',str(n2),'\n',str(n1))
        else:
            print('',str(n2),'\n',str(n3),'\n',str(n1))
            
