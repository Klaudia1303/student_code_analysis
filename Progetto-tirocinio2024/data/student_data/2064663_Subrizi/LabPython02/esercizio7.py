n1 = int(input('Inserici un numero intero: '))
n2 = int(input('Inserisci un numero intero: '))
n3 = int(input('Inserisci un numero intero: '))

if n1>=n2 and n1>=n3 and n2>=n3:
    print(str(n1)+'\n'+str(n2)+'\n'+str(n3))
elif n1>=n2 and n1>=n3 and n3>=n2:
    print(str(n1)+'\n'+str(n3)+'\n'+str(n2))

elif n2>=n1 and n2>=n3 and n1>=n3:
    print(str(n2)+'\n'+str(n1)+'\n'+str(n3))
elif n2>=n1 and n2>=n3 and n3>=n1:
    print(str(n2)+'\n'+str(n3)+'\n'+str(n1))

elif n3>=n1 and n3>=n2 and n1>=n2:
    print(str(n3)+'\n'+str(n1)+'\n'+str(n2))
else:
    print(str(n3)+'\n'+str(n2)+'\n'+str(n1))
