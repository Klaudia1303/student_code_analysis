k=True
p=0
while k:
    n=input('Intero o * ')
    if str(n)!='*':
        if int(n)>0:
            p=p+1
    else:
        k=False
print(p)
