x=int(input("inserire numero: "))
y=int(input("inserire numero: "))
k=x
if y==-1:
    print(-x)
if y==0 or x==0:
    print(0)
while y>1 and x!=0:
    k=k+x
    y=y-1
while y<-1 and x!=0:
    k=k+x
    y=y+1
    if y==-1:
        k=-k
if y!=-1:
    print(k)
