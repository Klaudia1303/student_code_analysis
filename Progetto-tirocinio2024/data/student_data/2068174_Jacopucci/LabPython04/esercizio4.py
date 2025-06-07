s=0
n=int(input('inserire un numero intero: '))
while (n!=0):
    if (n%3==0):
        s=s+n
        n=int(input('inserire un numero intero: '))
    else:
        n=int(input('inserire un numero intero: '))
print (s)
