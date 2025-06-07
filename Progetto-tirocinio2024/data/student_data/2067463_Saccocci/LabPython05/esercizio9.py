n=int(input('Inserire un intero dispari maggiore o uguale a 3:'))
print(n*'*')
for i in range(1,n-1):
    print('*'+(n-2)*' '+'*')
print(n*'*')
