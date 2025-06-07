a=input('immettere una stringa ')
b=input('immettere una stringa ')
c=input('immettere una stringa ')
while len(a)+len(b)!=len(c):
    a=b
    b=c
    c=input('immettere una stringa ')
print(a,b,c)
