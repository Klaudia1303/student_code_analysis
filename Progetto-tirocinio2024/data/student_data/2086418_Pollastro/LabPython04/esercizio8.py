s=str(input('inserire stringa: '))
x=0
y=1
while x!=y:
    t=s
    s=str(input('inserire stringa: '))
    x=t[-1]
    y=s[0]
print(t,s)
