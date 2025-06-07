n=int(input('Inserire numero: '))
t=2
while t<=n:
    d=2
    i=0
    while d<=t/2 and i==0:
        if t%d==0:
            i+=1
        d+=1
    if i==0:
        print(t)
    t+=1



