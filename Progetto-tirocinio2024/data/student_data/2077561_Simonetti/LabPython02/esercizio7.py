print('you will have to type three numbers and I will display them from bigger to smaller.')
n1=int(input('please type a number: '))
n2=int(input('please type another number: '))
n3=int(input('please type the last number: '))

if n1>n2 and n1>n3:
    if n2>n3:
        print('',n1,'\n',n2,'\n',n3)
    else:
        print('',n1,'\n',n3,'\n',n2)
elif n2>n1 and n2>n3:
    if n1>n3:
        print('',n2,'\n',n1,'\n',n3)
    else:
        print('',n2,'\n',n3,'\n',n1)
else:
    if n2>n1:
        print('',n3,'\n',n2,'\n',n1)
    else:
        print('',n3,'\n',n1,'\n',n2)

        
