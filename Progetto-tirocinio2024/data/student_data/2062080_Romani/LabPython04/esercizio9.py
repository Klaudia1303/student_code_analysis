n=int(input('Inserire intero: '))
i=0
x1=0
x2=1
while i<n and n>0:
    temp=x1
    x1=x2
    x2=temp+x2
    print(x1)
    i+=1
