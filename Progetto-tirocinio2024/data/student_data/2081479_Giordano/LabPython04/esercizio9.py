ending=int(input('insert number: '))
fibo1=0
fibo2=1
fibo3=1
for n in range(0,ending):
    print(fibo3)
    fibo3=fibo1+fibo2
    fibo1=fibo2
    fibo2=fibo3