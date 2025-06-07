n=input('please enter a number greater than 0: ')

while int(n)<0:
    print('please enter a positive value.')
    n=int(input('please enter a number greater than 0: '))
n=int(n)
if n==0:
    print(0)
elif n==1:
    print(1)
elif n>1:
    prevN1=1
    prevN2=1
    if n==2:
        print(prevN1,'\n',prevN2,sep='')
    else:
        print(prevN1,'\n',prevN2,sep='')
        i=2
        while not i==n:
            fib=prevN1+prevN2
            i+=1
            print(fib)
            prevN1=prevN2
            prevN2=fib
    
