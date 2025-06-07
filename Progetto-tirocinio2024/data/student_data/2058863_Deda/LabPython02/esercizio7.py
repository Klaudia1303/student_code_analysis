n1=int(input('Inserisci un numero intero n1 '))
n2=int(input('Inserisci un numero intero n2 '))
n3=int(input('Inserisci un numero intero n3 '))
sn1=str(n1)
sn2=str(n2)
sn3=str(n3)
if n1>=n2>=n3:
    print(sn1,'\n'+sn2,'\n'+sn3)
elif n1>=n3>=n2:
    print(sn1+'\n'+sn3+'\n'+sn2)
elif n2>=n1>=n3:
    print(sn2+'\n'+sn1+'\n'+n3)
elif n2>=n3>=n1:
    print(sn2+'\n'+sn3+'\n'+sn1)
elif n3>=n1>=n2:
    print(sn3+'\n'+sn1+'\n'+sn2)
elif n3>=n2>=n1:
    print(sn3+'\n'+sn2+'\n'+n1)
