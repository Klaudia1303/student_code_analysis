n1=int(input('inserire primo numero: '))
n2=int(input('inserire secondo numero: '))
n3=int(input('inserire terzo numero: '))
if n1<n2:
    if n2<n3:
        print(n3,'\n',n2,'\n',n1)
    elif n3<n2 and n3<n1:
        print(n2,'\n',n1,'\n',n3)
    elif n3<n2 and n1<n3:
        print(n2,'\n',n3,'\n',n1)
if n2<n1:
    if n1<n3:
        print(n3,'\n',n1,'\n',n2)
    elif n3<n1 and n2<n3:
        print(n1,'\n',n3,'\n',n2)
    elif n3<n1 and n3<n2:
        print(n1,'\n',n2,'\n',n3)

