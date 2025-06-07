n=int(input('Inserisci lato del quadrato dispari >=3 '))
for i in range(1,1+n):
    if i==1 or i==n:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')
