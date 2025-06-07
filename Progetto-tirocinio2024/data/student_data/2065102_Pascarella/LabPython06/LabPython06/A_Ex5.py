s=input()
x=1
y=0
z=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        x=x+1
        if y<=x:
            y=x
            z=s[i]

    else:
        if x>=y:
            y=x
            x=1 
print (z, y)
