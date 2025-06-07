n=int(input('inserisci un numero maggiore o uguale a 0 '))
f=1
if n>=0:
    while n>1:
        f=f*n
        n-=1
else:
    print('numero negativo')
print(f)
        
