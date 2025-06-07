n1=int(input('inserire numero intero: '))
n2=int(input('inserire numero intero: '))
n3=int(input('inserire numero intero: '))
if n1>n2 and n1>n3:
    if n2>n3:
        print(n1,n2,n3)
    else:
        print(n1,n3,n2)
if n2>n1 and n2>n3:
    if n1>n3:
        print(n2,n1,n3)
    else:
        print(n2,n3,n1)
if n3>n1 and n3>n2:
    if n2>n1:
        print(n3,n2,n1)
    else:
        print(n3,n1,n2)
