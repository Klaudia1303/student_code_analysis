n=int(input('Inserisci lato del quadrato >=2 '))
for i in range(n):
    if i==0 or i==(n-1):
        print('*'*n)
    else:
        for j in range(n):
            if j==(n-1):
                print('*')
            elif j==0 or j==i or j==(n-1-i):
                print('*',end='')
            else:
                print(' ',end='')
