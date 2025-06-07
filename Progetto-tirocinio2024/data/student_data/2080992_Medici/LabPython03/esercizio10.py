n=int(input('inserire un numero maggiore di 2: '))
b=2
while b<=n:
    j=2
    p=True
    while j<b and p:
        if b%j==0:
            p=False
        else:
            j+=1
    if p:
        print(b)
    b+=1
