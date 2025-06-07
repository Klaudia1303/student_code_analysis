s=input('inserire stringa: ')
x='a'
y='c'
z=1
c=True
while c:
    if x and y not in s:
        z=z+1
        s=input('inserire stringa: ')
    else:
        print(z)
        c=False
