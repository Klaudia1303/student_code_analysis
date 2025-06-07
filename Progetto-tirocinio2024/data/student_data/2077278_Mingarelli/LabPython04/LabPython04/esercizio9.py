n=int(input('inserisci un numero positivo '))
s=1
p=0
c=0
m=1
if n>0:
    print(s)
    while m<n:
        m+=1
        c=s+p
        p=s
        s=c
        print(c)
else:
    print('numero negativo')
