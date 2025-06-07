n = int(input('inserisci un intero: '))
p=0
q=1
f=0
x=1
while x<=n:
    p=q
    q=f
    f=p+q
    x=x+1
    print(f)
