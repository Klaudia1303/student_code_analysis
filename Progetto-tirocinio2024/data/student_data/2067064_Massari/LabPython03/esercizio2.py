x= int(input('scrivere un intero maggiore di zero:'))
n=int(x)
while n>0:
    if x%n==0:
        print(x//n)
        n-=1
    else:
        n-=1
        
