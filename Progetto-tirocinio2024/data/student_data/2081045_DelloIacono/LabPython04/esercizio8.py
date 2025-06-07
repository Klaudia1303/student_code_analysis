s=str(input('inserire una stringa: '))
t=str(input('inserire una stringa: '))
x=s[len(s)-1:]
y=t[0:1]
while not (x==y):
    s=t
    t=str(input('inserire una stringa: '))
    x=s[len(s)-1:]
    y=t[0:1]
print(s,t)
    
