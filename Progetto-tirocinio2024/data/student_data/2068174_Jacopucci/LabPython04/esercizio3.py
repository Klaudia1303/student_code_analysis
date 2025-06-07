s=0
n=(input('inserire un numero intero: '))
if (n!='*'):
    n=int(n)
while (n!='*'):
    if (n<0):
        s=s+n
        n=(input('inserire un numero intero: '))
        if (n!='*'):
            n=int(n)
    else:
        n=(input('inserire un numero intero: '))
        if (n!='*'):
            n=int(n)
print (s)
