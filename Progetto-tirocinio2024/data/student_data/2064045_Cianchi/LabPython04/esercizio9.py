n=int(input('inserire un intero maggiore di zero:'))
if n<=0:
    n=int(input('errato, inserire un intero maggiore di zero:'))
cont=0
f=''
x=1
y=0
while cont<n:
    f=x+y
    x=y
    y=f
    cont+=1
    print(f)
