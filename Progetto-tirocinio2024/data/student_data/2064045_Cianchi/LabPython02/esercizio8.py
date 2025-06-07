a=input('inserisci un intero')
a=int(a)
b=input('inserisci un secondo intero')
b=int(b)
c=input('inserisci un terzo intero')
c=int(c)
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b:
    if a==b==c:
    print('equilatero')
elif a==b or b==c or a==c:
    print('isoscele')
elif a!=b!=c:
    print('scaleno')
