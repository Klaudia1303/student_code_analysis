n1=int(input('numero 1: '))
n2=int(input('numero 2: '))
n3=int(input('numero 3: '))

if n1>=n2:
    if n1>=n3:
        if n2>=n3:
            print(str(n1) + "\n" + str(n2) + "\n" + str(n3))
        else:
            print(str(n1) + "\n" + str(n3) + "\n" + str(n2))
    else:
        print(str(n3) + "\n" + str(n1) + "\n" + str(n2))
else:
    if n3>=n2:
        print(str(n3) + '\n' + str(n2) + '\n' + str(n1))
    else:
        if n1>=n3:
            print(str(n2) + "\n" + str(n1) + "\n" + str(n3))
        else:
            print(str(n2) + "\n" + str(n3) + "\n" + str(n1))
            

    
       


