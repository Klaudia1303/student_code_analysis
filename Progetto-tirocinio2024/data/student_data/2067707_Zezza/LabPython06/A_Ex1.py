n1=int(input('n1>0: '))
n2=int(input('n2>0: '))
if n1>=n2:
    i=n1
else:
    i=n2
while i!=0:
    if n1%i==0 and n2%i!=0:
        print(i)
    i-=1
