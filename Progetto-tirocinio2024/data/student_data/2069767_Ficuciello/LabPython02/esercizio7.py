n1=int(input('Inserire un primo numero intero:' ))
n2=int(input('Inserire un secondo numero intero:' ))
n3=int(input('Inserire un terzo numero intero:' ))
print(max(n1,n2,n3))
if n1<n2 and n1>n3 or n1>n2 and n1<3:
    print(n1)
elif n2<n1 and n2>n3 or n2>n1 and n2<n3:
    print(n2)
elif n3<n1 and n3>n2 or n3>n1 and n3<n2:
    print(n3)
print(min(n1,n2,n3))

