n=int(input('inserire un intero (0 per terminare):'))
pos=0
while n!=0:
    if n%3==0:
        pos+=n
    n=int(input('inserire un intero (* per terminare):'))
print(pos)
