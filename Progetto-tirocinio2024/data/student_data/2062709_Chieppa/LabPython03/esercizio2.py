n=int(input('inserire numero= '))
x=1
if n>0:
    while n>x:
        if n%x==0:
            print(x)
        x=x+1
else:
    print('numero <0')
