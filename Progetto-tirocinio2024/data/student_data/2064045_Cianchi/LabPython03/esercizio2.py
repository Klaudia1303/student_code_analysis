n=int(input('inserire un numero maggiore di zero:'))
if n<=0:
    n=int(input('errato, inserire un numero maggiore di zero'))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i+=1
