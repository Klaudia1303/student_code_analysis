n=int(input('inserire un intero   '))
for i in range(n):
    for k in range(n):
        if i==0 or i==n-1:
            print('*',end='')
        elif k==0 or k==n-1:
            print('*',end='')
        elif k==i or k==n-1-i:
            print('*',end='')
        else:
            print(' ',end='')
    print()

            
