n1= int(input('Inserisci un numero intero: '))
n2= int(input('Inserisci un secondo numero intero: '))
n3= int(input('Inserisci un terzo numero intero: '))
if n1>=n2:
    if n1>=n3:
        if n2>=n3:
            print (n1,'\n',n2,'\n',n3)
        else:
            print (n1,'\n',n3,'\n',n2)
    else:
        print (n3,'\n',n1,'\n',n2)
else:
    if n2>=n3:
        if n3>=n1:
            print (n2,'\n',n3,'\n',n1)
        else:
            print (n2,'\n',n1,'\n',n3)
    else:
        print (n3,'\n',n2,'\n',n1)
