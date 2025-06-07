n1=int(input('Inserire il 1° numero '))
n2=int(input('Inserire il 2° numero '))
n3=int(input('Inserire il 3° numero '))
if n1<n2 and n2<n3:
    print(n1)
    print(n2)
    print(n3)
else:
    print(n3)
    print(n2)
    print(n1)
if n2<n1 and n1<n3:
    print(n2)
    print(n1)
    print(n3)
else:
    print(n3)
    print(n1)
    print(n2)
