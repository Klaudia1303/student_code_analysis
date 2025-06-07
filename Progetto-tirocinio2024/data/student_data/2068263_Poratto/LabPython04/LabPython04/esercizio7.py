s=input('inserisci una stringa')
c=33
a=0
b='!'
while c<255:
    d=chr(c)
    if s.count(d)>a:
        b=d
        a=s.count(b)
    elif s.count(chr(c))==a:
        if s.rfind(d)>s.rfind(b):
            b=d
            a=s.count(b)
    c+=1
print(b)
