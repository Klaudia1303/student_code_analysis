x=-1
while x<0:
    x=int(input('numero>0'))
i=1
while i<x+1:
    if x%i==0:
        print(i)
    i=i+1
