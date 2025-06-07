n=int(input('scrivi un numero: '))
d=2
c=True

while c and d<n:
    if n%d==0:
        print('il numero non è primo')
        c=False
    else:
        d=d+1

if c:
    print('il numero è primo')
    


