n=int(input('Inserire numero: '))
d=2
i=0
while d<=n/2 and i==0:
    if n%d==0:
        i+=1
    d+=1
if i==0:
    print('Numero primo')
else:
    print('Numero non primo')




