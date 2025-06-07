n=int(input('inserire un intero n maggiore di 0: '))
a=1
b=1
if n<=0:
    print('non hai inserito un intero maggiore di 0')
if n==1:
    print(1)
if n==2:
    print(1,'\n'+'1')
else:
    if n>2:
        print(a)
        print(b)
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(c, end='\n')
