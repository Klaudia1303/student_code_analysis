n1=int(input('inseqrire un numero intero '))
n2=int(input('inseqrire un numero intero '))
n3=int(input('inseqrire un numero intero '))
if n1>n2:
    if n3>(n1 and n2):
        print(n3,n1,n2)
    elif (n3>n2 and n3<n1):
        print(n1,n3,n2)
    else:
        print(n1,n2,n3)
if n2>n1:
    if n3>(n1 and n2):
        print(n3,n2,n1)
    elif (n2>n3 and n3>n1):
        print(n2,n3,n1)
    else:
        print(n1,n2,n3)

             
