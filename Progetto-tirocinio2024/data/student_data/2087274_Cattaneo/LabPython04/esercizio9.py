n=int(input('n='))
i=0
f=1
f1=0
while i<n:
    print(f)
    f=f+f1
    f1=f-f1
    i+=1
