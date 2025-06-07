n1 = input('Insert first number here: ')
n1 = int(n1)
n2 = input('Insert second number here: ')
n2 = int(n2)
n3 = input('Insert third number here: ')
n3 = int(n3)
if n1>n2 and n1>n3:
    if n2>n3:
        print(n1,n2,n3)
    elif n2<n3:
        print(n1,n3,n2)
elif n1<n2 and n1>n3:
    if n2>n3:
        print(n2,n1,n3)
    elif n2<n3:
        print(n3,n2,n1)
elif n1<n2 and n1<n3:
    if n2>n3:
        print(n2,n3,n1)
    elif n2<n3:
        print(n3,n2,n1)
else: print('Input non valido')
