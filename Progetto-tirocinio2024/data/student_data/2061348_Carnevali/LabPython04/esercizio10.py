s=input("inserire stringa: ")
t=input("inserire stringa: ")
r=input("inserire stringa: ")
x=int(len(s))
y=int(len(t))
z=int(len(r))
while x+y!=z:
    s=t
    t=r
    r=input("inserire stringa: ")
    x=int(len(s))
    y=int(len(t))
    z=int(len(r))
if x+y==z:
    print(s, t, r,)
    
