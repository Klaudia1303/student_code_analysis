a=str(input('inserire una stringa: '))
b=str(input('inserire una stringa: '))
c=str(input('inserire una stringa: '))
x=len(a)
y=len(b)
z=len(c)
while not(x+y==z):
    a=b
    b=c
    c=str(input('inserire una stringa: '))
    x=len(a)
    y=len(b)
    z=len(c)
print(a,b)
