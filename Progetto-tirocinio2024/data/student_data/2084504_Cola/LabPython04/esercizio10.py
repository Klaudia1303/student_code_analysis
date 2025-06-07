s=input('inserire una stringa: ')
u=input('inserire una stringa: ')
v=input('inserire una stringa: ')
x=len(s)
y=len(u)
z=len(v)
while x+y!=z:
    s=u
    u=v
    x=len(s)
    y=len(u)
    v=input('inserire una stringa: ')
    z=len(v)
print(s,u,v)
    
