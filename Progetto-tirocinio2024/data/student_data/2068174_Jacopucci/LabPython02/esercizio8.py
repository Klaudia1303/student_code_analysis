n1=input('inserire il primo valore: ')
n1=int(n1)
n2=input('inserire il primo valore: ')
n2=int(n2)
n3=input('inserire il primo valore: ')
n3=int(n3)
cat1=n3+n2
cat2=n1+n3
cat3=n2+n1
if (n1>=0 and n2>=0 and n3>=0 and n1<cat1 and n2<cat2 and n3<cat3):
    if (n1==n2 and n1==n3):
        print('il triangolo è equilatero')
    else:
        if((n1==n2 and n1!=n3) or (n2==n3 and n2!=n1)or (n3==n1 and n3!=n2)):
            print('il triangolo è isocele')
        else:
            print('il triangolo è scaleno')
else:
    print('input non valido')
