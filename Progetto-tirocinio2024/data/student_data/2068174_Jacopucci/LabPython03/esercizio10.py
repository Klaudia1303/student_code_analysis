n=int(input('inserire un numero intero: '))
c=1
s=0
while (c<=n):
    if (n%c==0):
        if(s==0):
            s+=c
            c+=1
        else:
            s+=c
            c+=1
            print(s)
    else:
        c+=1
