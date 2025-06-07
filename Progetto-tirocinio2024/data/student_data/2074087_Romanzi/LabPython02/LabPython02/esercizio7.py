n1=int(input('n1 '))
n2=int(input('n2 '))
n3=int(input('n3 '))
if n1>=n2 and n1>=n3:
    if n2>=n3:
        print(str(n1),'\n'+str(n2),'\n'+str(n3),'\n')
    else:
        print(str(n1),'\n'+str(n3),'\n'+str(n2),'\n')
if n2>=n1 and n2>=n3:
    if n1>=n3:
        print(str(n2),'\n'+str(n1),'\n'+str(n3),'\n')
    else:
        print(str(n2),'\n'+str(n3),'\n'+str(n1),'\n')
if n3>=n1 and n3>=n2:
    if n1>=n2:
        print(str(n3),'\n'+str(n1),'\n'+str(n2),'\n')
    else:
        print(str(n3),'\n'+str(n2),'\n'+str(n1),'\n')
        
