n = int(input('inserisci lato quadrato (intero dispari >=3): '))
space = n-2

for i in range(1, n+1):
    if i==1 or i==n:
        print('*'*n)
    else:
        print('*'+(' '*space)+'*')
