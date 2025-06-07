n=int(input('Inserire il lato del quadrato: '))
m=int(n/2)
for i in range(0,n):
    print('*',end='')
print()
for i in range(2,m+1):
    for k in range(1,n+1):
        if k==i or k==n-i+1:
            print('*',end='')
        elif k==1 or k==n:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(m+2,n):
    for k in range(1,n+1):
        if k==i or k==n-i+1:
            print('*',end='')
        elif k==1 or k==n:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(0,n):
    print('*',end='')
