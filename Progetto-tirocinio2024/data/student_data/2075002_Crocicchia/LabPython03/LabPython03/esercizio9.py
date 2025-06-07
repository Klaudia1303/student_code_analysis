n=int(input('inserire un numero intero: '))
div = 2
conta = 0
while div <= n/2 and conta==0:
    if n%div==0:
        conta+=1
    div+=1
if conta==0:
    print('numero primo')
else:
    print('numero non primo')