n=int(input('inserire un numero maggiore di 0:'))
i=1
div=0
while n>=i:
    if n%i==0:
        div+=1
    i+=1
if div==2:
    print('numero primo')
else:
    print('numero non primo')
