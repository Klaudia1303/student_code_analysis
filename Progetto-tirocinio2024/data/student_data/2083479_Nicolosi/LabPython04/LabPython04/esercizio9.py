n=int(input('Inserisci un numero n>0: '))
a=1
b=1
if n==1:
    print(a)
elif n>=2:
    print(a)
    print(b)
x=0
while x<=n:
    c=a+b
    print(c)
    a=b
    b=c
    x+=1