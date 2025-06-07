x=int(input('la dimensione del lato di un quadrato che sia un intero dispari maggiore o uguale a 3: '))
space='*'+ ' '*(x-2) +'*'
print('*'*x)
for i in range(1,x-1):
    print(space)
print('*'*x)
