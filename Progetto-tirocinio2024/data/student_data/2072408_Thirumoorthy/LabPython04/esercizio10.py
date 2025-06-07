s=input('inserire stringa')
x=input('inserire stringa')
y=input('inserire stringa')
while (len(s)+len(x)!=len(y)):
    s=x
    x=y
    y=input('inserire stringa')
print(s,x,y)
