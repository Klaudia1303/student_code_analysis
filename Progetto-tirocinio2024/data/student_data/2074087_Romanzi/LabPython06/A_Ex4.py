a=20
b=1
c=0
for i in range(1000):
    print('A: ',a,'B: ',b)
    c=c+1
    if a==b:
        print(c)
        break
    a=a+20
    b=b+i+2
