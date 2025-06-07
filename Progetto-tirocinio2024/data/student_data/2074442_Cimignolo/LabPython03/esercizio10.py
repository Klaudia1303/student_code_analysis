n=int(input('inserisci un numero N>1: '))

s=2
while s<=n:
    boo=True
    t=2
    while t<s:
        if s%t==0:
            boo=False
        t+=1
    if boo and s!=1:
        print(s)
    s+=1
