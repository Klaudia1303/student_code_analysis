n = int(input('Inserire numero: '))
print('*'*n)
l=n-3
for i in range(n-2):
    k=i

    print('*',end='')
    for j in range(n-2):
        if(j == k or j==l):
            print('*',end='')
        else:
            print(' ',end='')
    print('*')
    l = l - 1
print('*'*n)

