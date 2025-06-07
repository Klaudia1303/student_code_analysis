n=int(input('Intero maggiore o uguale a 0 '))
s=1
if n==0 or n==1:
    print(1)
else:
    for i in range(2,n+1):
        s=s*i
    print(s)
