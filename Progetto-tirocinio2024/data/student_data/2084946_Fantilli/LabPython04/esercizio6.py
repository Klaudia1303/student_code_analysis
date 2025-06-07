n = input()
n = int(n)
x = n
m = input()
m = int(m)
i = m
if m >= 0:
    while i>0:
        n+=x
        i-=1
        if i==1:
            print('prodotto:', n)
if m < 0:
    while i<0:
        n+=x
        i+=1
        if i==-1 and n>=0:
            print('prodotto:', -n)
        elif i==-1 and n<0:
            print('prodotto:', -n)
