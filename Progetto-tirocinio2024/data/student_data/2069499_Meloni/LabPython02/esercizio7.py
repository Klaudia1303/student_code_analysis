n1=int(input('Inserisci il primo numero '))
n2=int(input('Inserisci il secondo numero '))
n3=int(input('Inserisci il terzo numero '))

if(n1>n2>n3):
   print(n1,'\n',n2,'\n',n3)
elif(n3>n2>n1):
    print(n3,'\n',n2,'\n',n1)
elif(n2>n1>n3):
    print(n2,'\n',n1,'\n',n3)
elif(n2>n3>n1):
    print(n2,'\n',n3,'\n',n1)
elif(n1>n3>n2):
    print(n1,'\n',n3,'\n',n2)
elif(n3>n1>n2):
    print(n3,'\n',n1,'\n',n2)
