n=int(input('inserire un numero intero: '))
c=1
s=0
while (c<=n):
    if (n%c==0):
        s+=c
        c+=1
    else:
        c+=1
if (s==n+1):
    print('il numero è primo')
else:
    print ('il numero non è primo')
        
