n=int(input('inserire un numero maggiore o uguale a 3: '))
if n>3 and n%2==1:
    for i in range(1,n+1):
        if i==1 or i==n:
            print('*'*n)
        else:
            print(str('*')+str(' '*(n-2))+str('*'))
else:
    print('input non valido')
