s=str(input('inserire una tringa '))
i=1
x=0
z=0
k=0
while i<300:
    y=s.count(chr(i))
    if y>x:
        x=y
        z=chr(i)
        k=i
    if y==x:
        if s.find(chr(i))>s.find(chr(k)):
            x=y
            z=chr(i)
        elif s.find(chr(i))<s.find(chr(k)):
            ''
    i=i+1
print(z)

    
