n=input('inserire un intero (* per terminare):')
pos=0
while n!='*':
    if int(n)<0:
        pos+=int(n)
    n=input('inserire un intero (* per terminare):')
print(pos)
