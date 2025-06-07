n = input()
n = int(n)
n1=0
n2=1
if n>0:
    print(n2)
i=1
while i<n:
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    i+=1
