n=int(input('inserire numero intero: '))
x=2
c=0
while x<n:
    
    if n%x==0:
        x+= 1
        c+= 1
    else:
        x+= 1
if c>0:
    print('numero non primo')
else:
    print('numero primo')
