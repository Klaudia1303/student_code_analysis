n1=int(input('n1'))
n2=int(input('n2'))
n3=int(input('n3'))
if(n2>n1):
    n1,n2=n2,n1
if(n3>n1):
    n3,n1=n1,n3
if(n3>n2):
    n3,n2=n2,n3

print(n1,'\n',n2,'\n',n3)