n = int(input('insert integer n>1 here: '))
d = 2
c = 0
while d<=n:
    i = 2
    while i<=d:
        c = d%i
        if d==i:
            print(d)
        elif c==0:
            break
        i = i+1
    d = d+1
