s=input('inserire una stringa: ')
x=0
y=0
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        x=x+1
        if y<=x:
            z=s[i]
        continue
    if y<=x:
        y=x
        x=0
if y<=x:
    y=x
print(z,y+1)

