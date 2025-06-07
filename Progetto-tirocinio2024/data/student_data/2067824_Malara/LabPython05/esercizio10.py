n=int(input('inserire intermo >==2: '))
for y in range(n):
    for x in range(n):
        if y==0 or y==n-1:
            print('*',end='')
        elif x==0 or x==n-1:
            print('*',end='')
        elif y==x:
            print('*',end='')#diagnoale sinistra
        elif x+y==n-1:
            print('*',end='')#diag. destra
        else:  
            print(' ',end='')
    print()
       
