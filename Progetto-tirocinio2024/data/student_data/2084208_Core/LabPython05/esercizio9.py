n=int(input('Inserire la dimensione del lato di un quadrato: '))
print(n*'*')
for i in range(1,n-1):
    print('*'+(n-2)*' '+'*')
print(n*'*')

