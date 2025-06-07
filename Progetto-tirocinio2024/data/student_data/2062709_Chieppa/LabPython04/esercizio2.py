check=True
count=0
n=input('inserire numero intero (* per arrestare): ')
if n!='*':
    while check and n!='*':
        m=int(n)
        if m>0:
            count=count+1
            n=input('inserire numero intero (* per arrestare): ')
        if m<0:
            n=input('inserire numero intero (* per arrestare): ')
        elif n=='*':
            check=False
print(count)
