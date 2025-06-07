n=int(input('inserire un numero maggiore o uguale a 3: '))
if n>=2:
    for i in range(1,n+1):
        if i==1 or i==n:
            print('*'*n)
        else:
            print('*',end='')
            for j in range(2,n):
                if i==j or i==n+1-j:
                    print('*',end='')
                else:
                    print(' ',end='')
            print('*')
            
else:
    print('input non valido')
