i=1
fatt=1
n=int(input('inserire un numero intero: '))
while (n<=0):
    n=int(input('inserire un numero intero: '))
if (n==0 or n==1):
    fatt=1
else:
    while (i<=n):
        fatt=fatt*i
        i+=1
print(fatt) 
