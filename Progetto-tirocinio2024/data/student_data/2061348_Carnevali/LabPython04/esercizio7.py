s=input("inserire una stringa: ")
n=int(len(s)-1)
m=int(len(s))
x=int(0)
k="a"
while n>=0:
    y=int(s.count(s[n:m]))
    if y>=x:
        x=y
        k=s[n:m]
    n=n-1
    m=m-1
    if y>=x:
        x=y
print(k)
