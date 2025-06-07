n = input()
n = int(n)
if n==0 or n==1:
    print('n! = 1')
i=n
while i>=1:
    n *= (i-1)
    if i==2:
        print('n! =', n)
    i-=1
