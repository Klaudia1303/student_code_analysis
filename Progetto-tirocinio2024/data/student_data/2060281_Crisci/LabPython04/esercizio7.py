s=str(input("Inserire una stinga: "))
x=len(s)
i=0
app=0
while(i<x):
    n=s.count(s[i])
    if(n>=app):
        app=n
        carattere=s[i]
    i=i+1
print(carattere)
