s=str(input('inserire una stringa: '))
y=len(s)
i=0
app=0
while (i<y):
    n=s.count(s[i])
    if(n>=app):
        app=n
        carattere=s[i]
    i=i+1
print(carattere)
    
