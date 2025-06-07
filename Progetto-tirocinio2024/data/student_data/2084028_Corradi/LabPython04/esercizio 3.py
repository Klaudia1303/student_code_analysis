x=0
i=0
while x!='*':
    x=input('inserire numero intero')
    if x!='*':
        x=int(x)
        if x<0:
            i=i+x
print(i)
    
