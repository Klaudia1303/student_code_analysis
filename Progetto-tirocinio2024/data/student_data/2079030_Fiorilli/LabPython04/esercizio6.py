a=int(input('inserisci un valore intero: '))
b=int(input('inserisci un altro valore intero: '))
c=0
s=0
if b>=0 and a<0:
    d=a
    a=b
    b=d
elif a<0 and b<0:
    a=abs(a)
    b=abs(b)
while c<a:
    s=s+b
    c+=1
print (s)
