n1=input('inserire un numero intero: ')
n1=int(n1)
n2=input('inserire un numero intero: ')
n2=int(n2)
n3=input('inserire un numero intero: ')
n3=int(n3)
if n1!=n2 and n2!=n3 and n3!=n1: 
    if n1>n2 and n1>n3 and n2>n3:
        print(n1,n2,n3)
    elif n1>n2 and n1>n3 and n2>n3:
        print(n1,n2,n3)
    elif n2>n1 and n2>n3 and n1>n3:
        print(n2,n1,n3)
    elif n2>n1 and n2>n3 and n1<n3:
        print(n2,n3,n1)
    elif n3>n2 and n3>n1 and n1>n2:
        print(n3,n1,n2)
    elif n3>n2 and n3>n1 and n1<n2:
        print(n3,n2,n1)
else:
    print('i numeri sono uguali')
  
