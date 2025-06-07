n=int(input('inserisci un numero positivo dispari maggiore o uguale a 3: '))
for i in range(n):
    if i==0 or i==n-1: #primi e ultimi
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')
