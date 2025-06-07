n=int(input('inserire numero primo'))
c=1
d=0

while c<=n:
    if n%c==0:
        d += 1
    c += 1
if d==2:
    print('numero primo')
elif n!=1:
    print('numero non primo')
elif n==1:
    print('numero primo')
        

                
