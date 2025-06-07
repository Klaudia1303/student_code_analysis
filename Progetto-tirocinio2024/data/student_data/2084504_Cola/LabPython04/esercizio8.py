s=input('inserire una frase: ')
z=input('inserire una frase: ')
i=z[0]
a=s[-1]
if s!='' and z!='':
    while i!=a:
        s=z
        z=input('inserire una frase: ')
        i=z[0]
        a=s[-1]
    print(s,z)
else:
    print('input non valido')
    
    
