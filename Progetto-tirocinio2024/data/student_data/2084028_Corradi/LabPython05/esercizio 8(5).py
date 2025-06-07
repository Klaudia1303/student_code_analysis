b=int(input('inserire un numero dispari maggiore o uguale a 3'))
for i in range(1,b+1,2):
    n=(b-1)/2
    n=int(n)
    print((" "*n)+("*"*i)+(" "*n))
