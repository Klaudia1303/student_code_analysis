s=str(input('inserire una stringa: '))
c=33
x=0
a='!'
while c<255:
    b=chr(c)
    if s.count(b)>x:
        a=b
        x=s.count(b)
    elif s.count(chr(c))==x:
        if s.rfind(b)>s.rfind(a):
            a=b
            x=s.count(a)
    c+=1
print(a)
